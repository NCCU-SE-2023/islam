import os
import timeit
import unittest
from instagrapi import Client
from dotenv import find_dotenv, load_dotenv
from model.data_models.user_followers import UserFollowers
from scraper.instagrapi import instagrapi

from instagrapi.types import  UserShort
from mongoengine import  connect


# python unittest for instagrapi test
# Path: tests/test_instagrapi.py

class testInstagrapi(unittest.TestCase):

    def setUp(self):
        
        connect('islam')
        load_dotenv(find_dotenv())
        self.username = os.getenv("ig_username")
        self.password = os.getenv("ig_password")
        self.task_id = "F046918C9A07CA552308CDF5B2B3E1E1"
        

    def test_get_user_followers(self):
        testinstagrapi = instagrapi(self.username, self.password, self.task_id)
        followers_list = testinstagrapi.get_user_followers(self.username)
        print(followers_list)
  

    def test_get_user_following(self):
        testinstagrapi = instagrapi(self.username, self.password, self.task_id)
        following_list = testinstagrapi.get_user_following("testislam")
        print(following_list)
    
    def test_get_user_followers_and_following(self):
        testinstagrapi = instagrapi(self.username, self.password, self.task_id)
        followers_list = testinstagrapi.get_user_followers(self.username)
        following_list = testinstagrapi.get_user_following(self.username)
        print(followers_list)
        print(following_list)
    
    # test function time
    def test_time(self):
        followers = {'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[]),'58640502604': UserShort(pk='58640502604', username='amanpriyankameena', full_name='Aman Priyanka Meena',  profile_pic_url_hd=None, is_private=False, stories=[])}
        followers_list=[]
        def test_for():
            for user in followers:
                followers_list.append(followers[user].username)
        def test_value():            
            followers_list = [user.username for user in followers.values()]
        # followers_list = list(map(lambda d: d.get('key'), followers))
        print('value:', timeit.timeit(test_value))
        print('for:', timeit.timeit(test_for))
        
        

if __name__ == "__main__":
    unittest.main()