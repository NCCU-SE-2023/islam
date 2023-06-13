import logging
import os
import unittest
from unittest import suite
from instagrapi import Client

from dotenv import find_dotenv, load_dotenv
from model.data_models.user_followers import UserFollowers
from scraper.scraper_controller import MissionRunner

from scraper.mission.mission import scrape_followers_and_following
from model.task import Task, TaskType


class testWebScraper(unittest.TestCase):
    def setUp(self):

        load_dotenv(find_dotenv())
        self.username = os.getenv("ig_username")
        self.password = os.getenv("ig_password")

        # self.status_logger = logging.getLogger("STATUS_LOGGER")
        # self.status_handler = logging.FileHandler('logs/status.log')
        # self.status_handler.setLevel(logging.INFO)
        # self.status_logger.addHandler(self.status_handler)

        self.mission_logger = logging.getLogger("MISSION_LOGGER")
        self.mission_handler = logging.FileHandler("logs/mission.log")
        self.mission_handler.setLevel(logging.INFO)
        self.mission_logger.addHandler(self.mission_handler)

    def test_scrape_followers(self):
        cl = Client()
        cl.login(self.username, self.password)
        scraped_ig_id = "wjsn_transtation"
        user_id = cl.user_id_from_username(scraped_ig_id)
        followers = cl.user_followers_v1(user_id)
        # print(followers)
        count = 0
        followers_list = []
        for user in followers:
            count += 1
            followers_list.append(user.username)
            # print(user.username)
        raw_data = {
            "scraped_ig_id": scraped_ig_id,
            "followers_count": count,
            "followers_list": followers_list,
            "scrape_user": self.username,
            "scraped_task_id": "202CB962AC59075B964B07152D234B40",
        }
        UserFollowers.create_user_followers(raw_data)
        # self.assertIn(user_id, following)
        # self.assertEqual(following[user_id].username, "asphalt_kings_lb")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(testWebScraper("test_scrape_likes"))
    # suite.addTest(TestUserFollowers('test_create_user_followers_change'))
    # suite.addTest(TestUserFollowers('test_delete_user_followers_by_ig_id'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
