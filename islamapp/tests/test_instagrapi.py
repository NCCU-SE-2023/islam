import os
import time
import timeit
import unittest
from instagrapi import Client
from dotenv import find_dotenv, load_dotenv
from model.data_models.user_followers import UserFollowers
from scraper.instagrapi import instagrapi

from instagrapi.types import UserShort
from mongoengine import connect


# python unittest for instagrapi test
# Path: tests/test_instagrapi.py


class testInstagrapi(unittest.TestCase):
    def setUp(self):
        connect("islam")
        load_dotenv(find_dotenv())
        self.username = os.getenv("ig_username2")
        self.password = os.getenv("ig_password2")
        self.task_id = "F046918C9A07CA552308CDF5B2B3E1E1"

    def test_get_user_followers(self):
        testinstagrapi = instagrapi(self.username, self.password, self.task_id)
        followers_list = testinstagrapi.get_user_followers(self.username)
        print(followers_list)

    def test_get_user_following(self):
        testinstagrapi = instagrapi(self.username, self.password, self.task_id)
        following_list = testinstagrapi.get_user_following("testislam")
        print(following_list)

    def test_get_users_relative_followers_following(self):
        while True:
            testinstagrapi = instagrapi(self.username, self.password, self.task_id)
            return_val = testinstagrapi.get_users_relative_followers_following(
                self.username
            )
            print(return_val)
            print("res_list_count_following=" + return_val[1])
            print("following_list_count=" + return_val[3])
            # wait for ig query block
            time.sleep(700)
            if return_val[1] == return_val[3]:
                return "finished"


if __name__ == "__main__":
    unittest.main()
