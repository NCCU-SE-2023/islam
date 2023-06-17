import queue
from model.models import map_task_type_to_data_model
from model.task import Task
from scraper.driver import Driver
from scraper.mission.mission import map_task_type_to_mission
from multiprocessing import Process
from model.task import TaskStatus
from scraper.util import (
    SELENIUM_GRID_GRAPHQL_END_POINT,
    SELENIUM_GRID_HUB_ENDPOINT,
    MONGO_HOST,
    MONGO_PORT,
    MONGO_USER,
    MONGO_PASSWORD,
    grid_get_node_count,
    grid_get_ndoe_status,
)
from mongoengine import connect
from apscheduler.schedulers.blocking import BlockingScheduler


class ScraperCotroller(Process):
    def __init__(
        self,
        status_logger,
        mission_logger,
        run_period=1,
        run_local=True,
        local_driver_limit=3,
    ):
        super().__init__()
        self.tasks = queue.PriorityQueue()
        self.scrapers = {}
        self.running_missions = []
        self.running_tasks = []
        self.status_logger = status_logger
        self.mission_logger = mission_logger
        self.run_period = run_period
        self.run_local = run_local
        self.local_driver_limit = local_driver_limit

    def add_task(self, task: Task):
        priority = int(task.priority) if task.priority else 5
        self.tasks.put((priority, task))

    def fetch_task(self):
        tasks = Task.get_by_status("NEW")
        for task in tasks:
            self.add_task(task)

    def routine_job(self):
        if not self.run_local:
            # GRID MODE
            # 0. check avaliable scrapers
            nodes_status = grid_get_ndoe_status(SELENIUM_GRID_GRAPHQL_END_POINT)
            idle_node_counts = len(
                [x for x in nodes_status if x["sessionCount"] < x["maxSession"]]
            )
            node_counts = grid_get_node_count(SELENIUM_GRID_GRAPHQL_END_POINT)

            # 1. if task queue is empty fetch new tasks
            if self.tasks.empty():
                self.fetch_task()

            for running_mission in self.running_missions:
                if not running_mission.is_alive():
                    self.running_missions.remove(running_mission)

            # 2. Log process status
            self.status_logger.info(f"GRID MODE")
            self.status_logger.info(f"NODE COUNTS: {node_counts}")
            self.status_logger.info(f"QUEUING TASK COUNTS: {self.tasks.qsize()}")
            self.status_logger.info(f"RUNNING MISSIONS:{len(self.running_missions)}")
            self.status_logger.info("NODE STATUS :")
            for index, node in enumerate(nodes_status):
                self.status_logger.info(f"============NODE {index}============")
                self.status_logger.info(f"  id: {node['id']}")
                self.status_logger.info(
                    f"  session_count: {node['sessionCount']}/{node['maxSession']}"
                )
                self.status_logger.info(f"  status: {node['status']}")
            self.status_logger.info(f"==============================")

            # 3. if have idle nodes, start scraping
            while (not self.tasks.empty()) and (idle_node_counts > 0):
                task = self.tasks.get()[1]
                mission_runner = MissionRunner(
                    task, self.mission_logger, self.run_local
                )
                self.running_missions.append(mission_runner)
                idle_node_counts -= 1
                mission_runner.start()
        else:
            # LOCAL MODE
            self.status_logger.info(f"LOCAL MODE")
            # 0. check avaliable scrapers
            # nodes_status = grid_get_ndoe_status(SELENIUM_GRID_GRAPHQL_END_POINT)
            idle_node_counts = self.local_driver_limit - len(self.running_missions)

            # 1. if task queue is empty fetch new tasks
            if self.tasks.empty():
                self.fetch_task()

            for running_mission in self.running_missions:
                if not running_mission.is_alive():
                    self.running_missions.remove(running_mission)

            # 2. Log process status
            self.status_logger.info(f"NODE LIMIT: {self.local_driver_limit}")
            self.status_logger.info(f"QUEUING TASK COUNTS: {self.tasks.qsize()}")
            self.status_logger.info(f"RUNNING MISSIONS:{len(self.running_missions)}")
            self.status_logger.info(f"==============================")

            # 3. if have idle nodes, start scraping
            while (not self.tasks.empty()) and (idle_node_counts > 0):
                task = self.tasks.get()[1]
                mission_runner = MissionRunner(
                    task, self.mission_logger, self.run_local
                )
                self.running_missions.append(mission_runner)
                idle_node_counts -= 1
                mission_runner.start()

    def run(self):
        self.status_logger.info("Initializing scraper controller ...")
        self.status_logger.info(f"Connect to MongoDB {MONGO_HOST} {MONGO_PORT}")
        connect(
            db="islam",
            host=MONGO_HOST,
            port=int(MONGO_PORT),
            username=MONGO_USER,
            password=MONGO_PASSWORD,
        )
        self.status_logger.info("Initialization scraper controller success !")

        scheduler = BlockingScheduler()
        self.status_logger.info("Starting scheduler...")
        self.status_logger.info("Scheduler started !\n\n\n\n\n\n\n\n")
        scheduler.add_job(
            self.routine_job, "interval", args=[], seconds=self.run_period
        )
        scheduler.start()


class MissionRunner(Process):
    def __init__(self, task, logger, run_local=True):
        super().__init__()
        self.task = task
        self.logger = logger
        self.run_local = run_local

    def run(self):
        try:
            # 0. preparing
            connect(
                db="islam",
                host=MONGO_HOST,
                port=int(MONGO_PORT),
                username=MONGO_USER,
                password=MONGO_PASSWORD,
            )
            # 1. update task to running
            self.task.set_status(TaskStatus.RUNNING.value)

            self.mission = map_task_type_to_mission(self.task.type)
            self.data_model = map_task_type_to_data_model(self.task.type)
            self.logger.info(
                f"[START] task_id: {self.task.task_id} mission: {self.task.type} pid: {self.pid}"
            )
            # self.logger.info(f"[DRVER] task_id: {self.task.task_id} mission: {self.task.type} pid: {self.pid}")
            # if self.run_local:
            #     driver = Driver()
            # else:
            #     driver = Driver(SELENIUM_GRID_HUB_ENDPOINT)

            # 2. run mission
            result = self.mission({}, self.task)

            # save result to task
            if self.task.type != "FOLLOWER_AND_FOLLOWING":
                self.data_model.create(result)
            self.task.set_status(TaskStatus.FINISHED.value)
            self.logger.info(
                f"[FINSH] task_id:{self.task.task_id} mission:{self.task.type} pid:{self.pid}"
            )

        except Exception as exception:
            import traceback

            self.task.set_status(TaskStatus.ERROR.value)
            self.logger.error(f"[ERROR] task_id:{self.task.task_id} pid:{self.pid}")
            self.logger.error(f"        Msg: {traceback.format_exc()}")
        # finally:
        #     del driver
