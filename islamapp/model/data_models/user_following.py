from mongoengine import fields, Document

class UserFollowing(Document):
      
    scraped_user_id= fields.IntField(primary_key=True,required=True)
    scraped_user = fields.StringField(required=True)
    create_at = fields.DateTimeField(required=True)
    following_count = fields.IntField(required=True)
    following_list = fields.ListField(required=True)
    following_change_count = fields.IntField(required=True ,default=0)
    following_change_list = fields.ListField(required=True ,default=[])
    scrape_user_count = fields.IntField(required=True)
    scrape_user_list = fields.ListField(required=True)
    scraped_times = fields.IntField(required=True)
    scraped_task_list = fields.ListField(required=True)
    update_at = fields.DateTimeField(required=True)

    def to_json(self):
        returnDict = {}
        for key in self.__iter__():
            try:
                val = self.__getattribute__(key)
                returnDict[key] = val
            except:
                pass
        return returnDict