# connect to mongodb
import mongoengine
import datetime
import json
from user_followers import UserFollowers
from user_following import UserFollowing

cl = mongoengine.connect(db="islam", host="mongo-databse", port=27017,username="islam",password="islam")

followers_json = json.load(open("user_followers.json", "r"))
following_json = json.load(open("user_following.json", "r"))

for doc in followers_json:
    doc["user_followers_id"] = doc.pop("_id")
    doc["create_at"] = datetime.datetime.fromtimestamp(
        float(doc["create_at"]["$date"]["$numberLong"]) / 1000
    )
    user_followers = UserFollowers(**doc)
    user_followers.save(force_insert=True, connection=cl)

for doc in following_json:
    print(doc)
    doc["user_following_id"] = doc.pop("_id")
    doc["create_at"] = datetime.datetime.fromtimestamp(
        float(doc["create_at"]["$date"]["$numberLong"]) / 1000
    )
    user_following = UserFollowing(**doc)
    user_following.save(force_insert=True, connection=cl)
