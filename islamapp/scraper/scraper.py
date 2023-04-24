from scraper.driver import Driver
from enum import Enum
from scraper.mission.mission import *

class ScraperStatus(Enum):
    IDLE = "IDLE"
    RUNNING = "RUNNING"
    ERROR = "ERROR"

TASK_TYPE_MISSION_MAPPING = {
    "BASIC": scrape_followers_and_following,
}

class Scraper():
    """A scraper instance.
    """
    def __init__(self, scraper_id):
        self.browser = Driver()
        self.status = ScraperStatus.IDLE.value
        self.scraper_id = scraper_id
        self.result = None
        self.task = None
    
    def allocate_task(self, task):
        if self.status != ScraperStatus.IDLE.value:
            raise Exception("Scraper is not idle.")
        self.task = task

    def run(self):
        if self.status != ScraperStatus.IDLE.value:
            raise Exception("Scraper is not idle.")
        if self.task is None:
            raise Exception("Task is not allocated.")
        task_type = self.task.type
        if task_type not in TASK_TYPE_MISSION_MAPPING.keys():
            raise Exception("Task type is not supported.")
        mission = TASK_TYPE_MISSION_MAPPING[task_type]
        # run task
        try:
            self.status = ScraperStatus.RUNNING.value
            self.result = mission(self.browser, self.task)
            self.status = ScraperStatus.IDLE.value
        except Exception as exception:
            self.status = ScraperStatus.ERROR.value
            raise Exception(exception)
    
