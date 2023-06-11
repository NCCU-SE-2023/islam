from instagrapi import Client
from time import sleep
import random
from model.data_models.user_followers import UserFollowers
from model.data_models.user_following import UserFollowing


class Instagrapi:
    
    def __init__(self, username, password, task_id):
        self.username = username
        self.password = password
        self.task_id = task_id
        self.cl = Client()
        # login
        self.cl.login(username, password)
        
        
    def get_user_followers(self, scraped_ig_id):
        user_id = self.cl.user_id_from_username(scraped_ig_id)
        # limit to 100 followers
        followers = self.cl.user_followers(user_id, amount=100)
        followers_list=[]
        for user in followers:
            followers_list.append(followers[user].username)
        
        raw_data = {
            "scraped_ig_id": scraped_ig_id,
            "followers_count": len(followers_list),
            "followers_list": followers_list,
            "scrape_user": self.username,
            "scraped_task_id": self.task_id,
        }
        return raw_data
    
    def get_user_following(self, scraped_ig_id):
        user_id = self.cl.user_id_from_username(scraped_ig_id)
        print(user_id)
        # limit to 100 following
        following = self.cl.user_following(user_id, amount=100)
        following_list=[]
        for user in following:
            following_list.append(following[user].username)
            
        raw_data = {
            "scraped_ig_id": scraped_ig_id,
            "following_count": len(following_list),
            "following_list": following_list,
            "scrape_user": self.username,
            "scraped_task_id": self.task_id,
        }
        return raw_data
    
    def get_seond_step_followers_and_following(self, user_following: UserFollowing):
        following_list = user_following.following_list

        for i, user_id in enumerate(following_list):

            if i >=30:
                break

            # limit to 100 following
            following = self.cl.user_following(user_id, amount=100)
            raw_following_list=[]
            for user in following:
                raw_following_list.append(following[user].username)
                
            raw_data = {
                "scraped_ig_id": user_id,
                "following_count": len(raw_following_list),
                "following_list": raw_following_list,
                "scrape_user": self.username,
                "scraped_task_id": self.task_id,
            }
            UserFollowing.create(raw_data)
            print(f"Following of {user_id} OK")

            sleep(random.random()*3)

            # limit to 100 followers
            followers = self.cl.user_followers(user_id, amount=100)
            followers_list=[]
            for user in followers:
                followers_list.append(followers[user].username)
            
            raw_data = {
                "scraped_ig_id": user_id,
                "followers_count": len(followers_list),
                "followers_list": followers_list,
                "scrape_user": self.username,
                "scraped_task_id": self.task_id,
            }
            UserFollowers.create(raw_data)
            print(f"Followers of {user_id} OK")

            sleep(random.random()*3)
        
