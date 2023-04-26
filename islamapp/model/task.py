from mongoengine import fields, Document
from enum import Enum
import time
from hashlib import md5
import random

class TaskStatus(Enum):
    NEW = "NEW"
    RUNNING = "RUNNING"
    FINISHED = "FINISHED"
    ERROR = "ERROR"

class TaskType(Enum):
    BASIC = "BASIC"
    FOLLOWERS = "FOLLOWERS"
    FOLLOWING = "FOLLOWING"
    LIKES = "LIKES"
    COMMENTS = "COMMENTS"
    TAG_ME = "TAG_ME"
    I_TAG = "I_TAG"  
    TEST = "TEST" # For Task API testing

class TaskException(Exception):
    pass

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
    
    @staticmethod
    def create_task(user_id, type, task_detail={}):
        if type not in [type.value for type in TaskType]:
            raise TaskException(f"Invalid task type {type}")
        
        create_at = time.time()
        task_id = md5(str(create_at).join(user_id).join(str(random.random())).encode()).hexdigest()
        create_at = int(create_at)
        update_at = create_at
        status = TaskStatus.NEW.value
        
        task = Task(task_id=task_id, type=type, create_user=user_id, task_detail=task_detail, create_at=create_at, update_at=update_at, status=status)
        task.save()
        return task
    
    
    def set_status(self, status):
        if status not in [status.value for status in TaskStatus]:
            raise TaskException(f"Invalid task status {status}")
        self.status = status
        self.update_at =int(time.time())

    def set_errmsg(self,msg="error"):
        self.error_msg = msg
        self.update_at = int(time.time())

    def retry_task(self):
        if(self.priority>=5):
            self.status=TaskStatus.ERROR.value
            raise TaskException(f"retry time exceeded")
        self.retry_times+=1
        self.priority+=1
        self.set_status("NEW")

    @staticmethod
    def get_by_status(status, userId=None):
        if status not in TaskStatus.value:
            raise TaskException(f"Invalid task status {status}")
        if userId is not None:
            return Task.objects(status=status, create_user=userId)
        else:
            return Task.objects(status=status)
    
    @staticmethod
    def get_by_create_user(userId):
        return Task.objects(create_user=userId)