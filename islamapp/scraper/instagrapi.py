from instagrapi import Client

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
        # limit to 50 followers
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
        # limit to 50 following
        following = self.cl.user_following(user_id, amount=30)
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