from mongoengine import fields, Document

class Task(Document):
    # constant field
    task_id = fields.StringField(primary_key=True, required=True)
    type = fields.StringField(required=True)
    create_user = fields.StringField(required=True)
    task_detail = fields.DictField(required=False)
    create_at = fields.IntField(required=True)
    # variable field
    status = fields.StringField(required=True)
    update_at = fields.IntField(required=True)
    error_msg = fields.DictField(required=False)
    priority = fields.IntField(required=False, default=0, min_value=-1, max_value=5)
    retry_times = fields.IntField(required=True, default=0)

    def to_json(self):
        returnDict = {}
        for key in self.__iter__():
            try:
                val = self.__getattribute__(key)
                returnDict[key] = val
            except:
                pass
        return returnDict