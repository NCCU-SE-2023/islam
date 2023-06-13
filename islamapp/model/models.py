from model.user import User
from model.task import TaskType
from model.data_models.user_post_like import UserPostLike
from model.data_models.user_followers import UserFollowers
from model.data_models.user_following import UserFollowing


def map_task_type_to_data_model(task_type):
    if task_type == TaskType.LIKES.value:
        return UserPostLike
    elif task_type == TaskType.FOLLOWERS.value:
        return UserFollowers
    elif task_type == TaskType.FOLLOWING.value:
        return UserFollowing
