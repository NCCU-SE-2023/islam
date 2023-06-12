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
        # check the database if the user is already scraped
        followers_list_object = UserFollowers.get_latest_user_followers_by_ig_id(scraped_ig_id)      
        followers_list=[]
        if followers_list_object==None:
            user_id = self.cl.user_id_from_username(scraped_ig_id)
            # TODO: change the limit to 100
            followers = self.cl.user_followers(user_id,amout=10)
            for user in followers:
                followers_list.append(followers[user].username)
            
            raw_data = {
                "scraped_ig_id": scraped_ig_id,
                "followers_count": len(followers_list),
                "followers_list": followers_list,
                "scrape_user": self.username,
                "scraped_task_id": self.task_id,
            }
            UserFollowers.create_user_followers(raw_data)
        else:   
            followers_list = followers_list_object.followers_list 
        
        return followers_list
    
    def get_user_following(self, scraped_ig_id):
        # check the database if the user is already scraped
        following_list_object = UserFollowing.get_latest_user_following_by_ig_id(scraped_ig_id)
        following_list=[]
        if following_list_object==None:          
            user_id = self.cl.user_id_from_username(scraped_ig_id)
            # limit to 30 following
            # TODO: change the limit to 100
            following = self.cl.user_following(user_id,amout=10)
            for user in following:
                following_list.append(following[user].username)               
            raw_data = {
                "scraped_ig_id": scraped_ig_id,
                "following_count": len(following_list),
                "following_list": following_list,
                "scrape_user": self.username,
                "scraped_task_id": self.task_id,
            }
            UserFollowing.create_user_following(raw_data) 
        else:
            following_list = following_list_object.following_list   
        
        return following_list
    
    def get_users_relative_followers_following(self, scraped_ig_id):
        """_summary_

        Args:
            scraped_ig_id (str): _description_

        Returns:
            _type_: sucess scraped followers number, total scraped followers number
                , sucess scraped following number, total scraped following number
        """        
        
        followers_list = self.get_user_followers(scraped_ig_id)
        following_list = self.get_user_following(scraped_ig_id)
        # check the list which need to be scraped
        res_list = following_list +list(set(followers_list)-set(following_list))
        res_list_count_followers = len(res_list)
        res_list_count_following = len(res_list)
        # error list
        error_list = []
        
        for user in res_list:
                     
            try:
                self.get_user_followers(user)
                    
            except Exception as e: 
                error_list.append(e)
                res_list_count_followers = res_list_count_followers - 1
                pass
            
            try:
                self.get_user_following(user)             
            except Exception as e: 
                error_list.append(e)
                res_list_count_following = res_list_count_following - 1
                pass

        return  res_list_count_followers,res_list_count_following,len(res_list),len(following_list),res_list,error_list
    
    def get_seond_step_followers_and_following(self, user_following: UserFollowing):
        following_list = user_following.following_list

        for i, user_id in enumerate(following_list):

            if i >=50:
                break
            ig_id = self.cl.user_id_from_username(user_id)

            if len(UserFollowing.objects(scraped_ig_id=user_id)) == 0:
                try:
                    following = self.cl.user_following(ig_id, amount=150)
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
                except:
                    import traceback
                    traceback.print_exc()
                    print(f"Following of {user_id} ERROR")
                    return

                sleep(random.random()*3)

            # limit to 100 followers
            if len(UserFollowers.objects(scraped_ig_id=user_id)) == 0:
                try:
                    followers = self.cl.user_followers(ig_id, amount=150)
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
                except:
                    import traceback
                    traceback.print_exc()
                    print(f"Followers of {user_id} ERROR")
                    return

                sleep(random.random()*3)
