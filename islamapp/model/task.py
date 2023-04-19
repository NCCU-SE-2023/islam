from mongoengine import fields, Document

class Task(Document):
    task_id = fields.StringField(primary_key=True, required=True)
    status = fields.StringField(required=True)
    type = fields.StringField(required=True)
    task_detail = fields.DictField(required=False)
    create_user = fields.StringField(required=True)
    create_at = fields.IntField(required=True)
    update_at = fields.IntField(required=True)
    error_msg = fields.DictField(required=False)

    def to_json(self):
        returnDict = {}
        for key in self.__iter__():
            try:
                val = self.__getattribute__(key)
                returnDict[key] = val
            except:
                pass
        return returnDict