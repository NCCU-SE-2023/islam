import queue
from model.task import Task
from scraper.driver import Driver
from scraper.scraper import Scraper
from scraper.mission.mission import map_task_type_to_mission
from multiprocessing import Process
from model.task import TaskStatus
from scraper.util import (
    SELENIUM_GRID_GRAPHQL_END_POINT,
    SELENIUM_GRID_HUB_ENDPOINT, 
    MONGO_HOST, MONGO_PORT, 
    grid_get_node_count,
    grid_get_ndoe_status
)
from mongoengine import connect
from apscheduler.schedulers.blocking import BlockingScheduler

class ScraperCotroller(Process):
    def __init__(self, status_logger, mission_logger):
        super().__init__()
        self.tasks = queue.PriorityQueue()
        self.scrapers = {}
        self.running_missions = []
        self.running_tasks = []
        self.status_logger = status_logger
        self.mission_logger = mission_logger

    def _launch_scrapers(self, scraper_num=1):
        for id in range(scraper_num):
            self.scrapers[id] = Scraper(id)

    def add_task(self, task: Task):
        priority = int(task.priority) if task.priority else 5
        self.tasks.put((priority, task))
    
    def fetch_task(self):
        tasks = Task.get_by_status("NEW")
        for task in tasks:
            self.add_task(task)

    def routine_job(self):
        # 1. check avaliable scrapers
        nodes_status = grid_get_ndoe_status(SELENIUM_GRID_GRAPHQL_END_POINT)
        idle_node_counts = len([x for x in nodes_status if x["sessionCount"] < x["maxSession"]])
        node_counts = grid_get_node_count(SELENIUM_GRID_GRAPHQL_END_POINT)
        self.status_logger.info(f"NODE COUNTS: {node_counts}")
        self.status_logger.info(f"RUNNING MISSIONS:{len(self.scrapers)}")
        self.status_logger.info("NODE STATUS :")
        for index,node in enumerate(nodes_status):
            self.status_logger.info(f"============NODE {index}============")
            self.status_logger.info(f"  id: {node['id']}")
            self.status_logger.info(f"  session_count: {node['sessionCount']}/{node['maxSession']}")
            self.status_logger.info(f"  status: {node['status']}")

        # 2. if task queue is empty fetch new tasks
        if self.tasks.empty():
            self.fetch_task()
        self.status_logger.info(f"QUEUING TASK COUNTS: {self.tasks.qsize()}")

        # 3. if have idle nodes, start scraping
        while (not self.tasks.empty() ) and idle_node_counts > 0:
            task = self.tasks.get()[1]
            mission_runner = MissionRunner(task, self.mission_logger)
            self.running_missions.append(mission_runner)
            mission_runner.start()
            idle_node_counts -= 1

    def run(self):
        self.status_logger.info("Initializing scraper controller ...")
        self.status_logger.info(f"Connect to MongoDB {MONGO_HOST} {MONGO_PORT}")
        connect(db="islam", host=MONGO_HOST, port=int(MONGO_PORT))

        scheduler = BlockingScheduler()
        self.status_logger.info("Starting scheduler...")
        scheduler.add_job(self.routine_job, 'interval', args=[], seconds=5)
        scheduler.start()

class MissionRunner(Process):
    def __init__(self, task, logger):
        super().__init__()
        self.task = task
        self.logger = logger

    def run(self):
        try:
            # 0. preparing
            connect(db="islam", host=MONGO_HOST, port=int(MONGO_PORT))
            self.mission = map_task_type_to_mission(self.task.type)
            self.logger.info(f"[START] task_id:{self.task.task_id} mission:{self.mission.__name__} pid:{self.pid}")
            self.logger.info(f"[DRIVER] task_id:{self.task.task_id} mission:{self.mission.__name__} pid:{self.pid}")
            driver = Driver(SELENIUM_GRID_HUB_ENDPOINT)
            # 1. update task to running
            self.task.set_status(TaskStatus.RUNNING.value)
            # 2. run mission
            result = self.mission(driver.driver, self.task)

            if result == "ERROR": # change to mission_error class with error message
                self.logger.error(f"[ERROR] task_id:{self.task.task_id} mission:{self.mission.__name__} pid:{self.pid}")
                self.task.set_status(TaskStatus.ERROR.value)
                # update error msg
            else:
                self.task.set_status(TaskStatus.SUCCESS.value)
                # save result to task
                self.logger.info(f"[SUCCESS] task_id:{self.task.task_id} mission:{self.mission.__name__} pid:{self.pid}")
        except Exception as exception:
            self.logger.error(f"[ERROR] task_id:{self.task.task_id} pid:{self.pid}")
            self.logger.error(str(exception))
            self.task.set_status(TaskStatus.ERROR.value)
        finally:
            del driver