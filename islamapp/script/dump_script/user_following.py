from datetime import datetime
from hashlib import md5
import random
from mongoengine import fields, Document
import mongoengine

cl = mongoengine.connect(db="islam", host="mongo-databse", port=27017,username="islam",password="islam")
class UserFollowing(Document):
    meta = {
        "collection": "user_followings",
        "strict": False,
        "connection": cl,
    }

    # Convert this field for consistency
    user_following_id = fields.StringField(primary_key=True, required=True)
    scraped_ig_id = fields.StringField(required=True)
    create_at = fields.DateTimeField(required=True)
    following_count = fields.IntField(required=True)
    following_list = fields.ListField(required=True)
    following_change_count = fields.IntField(required=True, default=0)
    following_change_list = fields.ListField(required=True, default=[])
    scrape_user_count = fields.IntField(required=True)
    scrape_user_list = fields.ListField(required=True)
    scraped_times = fields.IntField(required=True)
    scraped_task_list = fields.ListField(required=True)

    @staticmethod
    def create(raw_data):
        create_at = datetime.now()
        user_following_id = md5(
            str(create_at)
            .join(raw_data["scraped_ig_id"])
            .join(str(random.random()))
            .encode()
        ).hexdigest()
        latest_user_following = UserFollowing.get_latest_user_following_by_ig_id(
            raw_data["scraped_ig_id"]
        )
        following_change_count = 0
        following_change_list = ["none"]
        scrape_user_count = 1
        scrape_user_list = [raw_data["scrape_user"]]
        scraped_times = 1
        scraped_task_list = [raw_data["scraped_task_id"]]

        # The below code is used to calculate the change in the count of following and the list of following added and removed
        if latest_user_following is not None:
            following_change_count = (
                raw_data["following_count"] - latest_user_following.following_count
            )
            if following_change_count == 0:
                following_change_list = ["none"]
            else:
                following_add_list = list(
                    set(raw_data["following_list"])
                    - set(latest_user_following.following_list)
                )
                following_minus_list = list(
                    set(latest_user_following.following_list)
                    - set(raw_data["following_list"])
                )
                following_change_list.clear()
                following_change_list = ["added_" + i for i in following_add_list] + [
                    "removed_" + i for i in following_minus_list
                ]

            if raw_data["scrape_user"] not in latest_user_following.scrape_user_list:
                scrape_user_count = latest_user_following.scrape_user_count + 1
                scrape_user_list.extend(latest_user_following.scrape_user_list)
            else:
                scrape_user_count = latest_user_following.scrape_user_count
                scrape_user_list = latest_user_following.scrape_user_list

            if (
                raw_data["scraped_task_id"]
                not in latest_user_following.scraped_task_list
            ):
                scraped_times = latest_user_following.scraped_times + 1
                scraped_task_list.extend(latest_user_following.scraped_task_list)
            else:
                scraped_times = latest_user_following.scraped_times
                scraped_task_list = latest_user_following.scraped_task_list

        userfollowing = UserFollowing(
            user_following_id=user_following_id,
            create_at=create_at,
            scraped_ig_id=raw_data["scraped_ig_id"],
            following_count=raw_data["following_count"],
            following_list=raw_data["following_list"],
            following_change_count=following_change_count,
            following_change_list=following_change_list,
            scrape_user_count=scrape_user_count,
            scrape_user_list=scrape_user_list,
            scraped_times=scraped_times,
            scraped_task_list=scraped_task_list,
        )

        userfollowing.save(connection=cl)

        return userfollowing

    @staticmethod
    def get_latest_user_following_by_ig_id(scraped_ig_id: str):
        try:
            return (
                UserFollowing.objects(scraped_ig_id=scraped_ig_id)
                .order_by("-create_at")
                .first()
            )
        except Exception as e:
            print("Error: ", str(e))

    @staticmethod
    def get_all_user_following_by_ig_id(scraped_ig_id: str):
        """
        Get all user following by ig id
        :param scraped_ig_id:
        :return: UserFollowing queryset
        """
        try:
            # Get user following by ig id
            userFollowing = UserFollowing.objects(scraped_ig_id=scraped_ig_id)
            # If user following exists
            if userFollowing:
                # Return user following
                return userFollowing
            else:
                # Else return none
                return None

        except Exception as e:
            # Print error message
            print(e)
            # Return none
            return None

    # maybe useful in the future, but not now
    # def update_user_following(user_following_id: str):
    #     return Userfollowing.objects(user_following_id=user_following_id).update_one()

    @staticmethod
    def delete_user_following_by_ig_id(scraped_ig_id: str):
        try:
            userFollower = (
                UserFollowing.objects(scraped_ig_id=scraped_ig_id)
                .order_by("-create_at")
                .first()
            )
            if userFollower:
                userFollower.delete()
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
