from datetime import datetime
from hashlib import md5
import random
from mongoengine import fields, Document

class UserPostLike(Document):

    #Convert this field for consistency
    user_post_like_id= fields.StringField(primary_key=True,required=True)
    scraped_ig_id= fields.StringField(required=True)
    create_at = fields.DateTimeField(required=True)
    post_count = fields.IntField(required=True,default=0)
    post_like_dict = fields.DictField(required=True,default={})
    scrape_user_count = fields.IntField(required=True)
    scrape_user_list = fields.ListField(required=True)
    scraped_times = fields.IntField(required=True)
    scraped_task_list = fields.ListField(required=True)


        
    @staticmethod
    def create(raw_data):
        
        create_at= datetime.now()
        user_post_like_id = md5(str(create_at).join(raw_data["scraped_ig_id"]).join(str(random.random())).encode()).hexdigest()
        latest_user_post_like = UserPostLike.get_latest_user_post_like_by_ig_id(raw_data["scraped_ig_id"]) 
             
        scrape_user_count=1
        scrape_user_list=[raw_data["scrape_user"]]
        scraped_times=1
        scraped_task_list=[raw_data["scraped_task_id"]]
        
        # The below code is used to calculate the change in the count of post_like and the list of post_like added and removed
        if latest_user_post_like is not None:
            
            if raw_data['scrape_user'] not in latest_user_post_like.scrape_user_list:
                scrape_user_count=latest_user_post_like.scrape_user_count + 1
                scrape_user_list.extend(latest_user_post_like.scrape_user_list)
            else:
                scrape_user_count=latest_user_post_like.scrape_user_count
                scrape_user_list=latest_user_post_like.scrape_user_list
            
            if raw_data['scraped_task_id'] not in latest_user_post_like.scraped_task_list:
                scraped_times=latest_user_post_like.scraped_times + 1
                scraped_task_list.extend(latest_user_post_like.scraped_task_list)
            else:
                scraped_times=latest_user_post_like.scraped_times
                scraped_task_list=latest_user_post_like.scraped_task_list
        
        userpost_like = UserPostLike(user_post_like_id=user_post_like_id, create_at=create_at, 
                                        scraped_ig_id=raw_data["scraped_ig_id"], post_count=raw_data["post_like_count"] , 
                                        post_like_dict=raw_data["post_like_dict"] , scrape_user_count=scrape_user_count,
                                        scrape_user_list=scrape_user_list,scraped_times=scraped_times, scraped_task_list=scraped_task_list)

        userpost_like.save()
        
        return userpost_like

    @staticmethod
    def get_latest_user_post_like_by_ig_id(scraped_ig_id: str):
        try:
            return UserPostLike.objects(scraped_ig_id=scraped_ig_id).order_by('-create_at').first()
        except Exception as e:
            print('Error: ', str(e))
            
    @staticmethod
        
    def get_all_user_post_like_by_ig_id(scraped_ig_id: str):
            """
            Get all user post_like by ig id
            :param scraped_ig_id:
            :return: UserPostLike queryset
            """
            try:
                # Get user post_like by ig id
                userPostLike = UserPostLike.objects(scraped_ig_id=scraped_ig_id)
                # If user post_like exists
                if userPostLike:
                    # Return user post_like
                    return userPostLike
                else:
                    # Else return none
                    return None

            except Exception as e:
                # Print error message
                print(e)
                # Return none
                return None

    # maybe useful in the future, but not now
    # def update_user_post_like(user_post_like_id: str):
    #     return Userpost_like.objects(user_post_like_id=user_post_like_id).update_one()

    @staticmethod
    def delete_user_post_like_by_ig_id(scraped_ig_id: str):
        try:
            userPostLike = UserPostLike.objects(scraped_ig_id=scraped_ig_id).order_by('-create_at').first()
            if userPostLike:
                userPostLike.delete()
                return 1
        except Exception as e:
            print(e)
            
    def to_json(self):
        returnDict = {}
        for key in self.__iter__():
            try:
                val = self.__getattribute__(key)
                returnDict[key] = val
            except:
                pass
        return returnDict