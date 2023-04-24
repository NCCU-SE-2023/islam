import queue
from model.task import Task
from service.task_service import _get_new_tasks
from scraper.scraper import Scraper

class ScraperCotroller():
    def __init__(self):
        self.tasks = queue.PriorityQueue()
        self.running_tasks = []
        self.scrapers = {}
        self.idle_scrapers = set()
        self.running_scrapers = set()
        self.error_scrapers = set()

    def launch_scrapers(self, scraper_num=1):
        for id in range(scraper_num):
            self.scrapers[id] = Scraper(id)

    def add_task(self, task: Task):
        priority = int(task.priority) if task.priority else 5
        self.tasks.put( priority, task )
    
    def fetch_task(self):
        tasks = _get_new_tasks()
        for task in tasks:
            self.add_task(task)

    def run_task(self):
        try:
            # allocate resources
            task = self.tasks.get(blocking=True, timeout=5)
            self.tasks.task_done()
            ilde_scraper = self.idle_scrapers.pop()
            self.running_scrapers.add(ilde_scraper)
            self.running_tasks.append(task.task_id)
            # run task
            # save result
        except queue.Empty:
            print("No task in queue.")

