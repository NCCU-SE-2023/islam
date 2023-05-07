from model.user import User
from model.task import TaskType
from model.data_models.user_post_like import UserPostLike

def map_task_type_to_data_model(task_type):
    if task_type == TaskType.LIKES.value:
        return UserPostLike