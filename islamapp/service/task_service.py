from model.task import Task
from service.util import (
    _gen_error_response,
    authenticate_user,
    INTERNAL_SERVER_ERROR,
    MALEFORMED_REQUEST,
)
from hashlib import md5
import random
import time
from enum import Enum
from flask import jsonify

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


@authenticate_user(check_existence=True)
def new_task(request):
    """
    Request:
        headers:
        {
            "user_id": "dummy-user-id"
        }
        body:
        {
            "task_info":{
                "type": "BASIC",
                "task_detail":{
                    "account": "ig_account",
                    "password": "ig_password"
                }
            }
        }
    Returns:
        headers:
        {
            "task_id": "dummy-user-id"
        }
        body:
        {
            “task_info”: {
                “task_id”: “task-id-123”,
                “task_status”: “NEW”,
                …
            }
        }
    """
    try:
        user_id = request.headers.get("user_id")
        task_info = request.json.get("task_info")
        type = task_info.get("type")
        task_detail = task_info.get("task_detail")

        # check type in TaskType
        if type not in [task_type.value for task_type in TaskType]:
            return _gen_error_response(
                status_code=400,
                error_code=MALEFORMED_REQUEST,
                message=f"Task type {type} is not supported",
            )
        
        create_at = time.time()
        task_id = md5(str(create_at).join(user_id).join(str(random.random())).encode()).hexdigest()
        create_at = int(create_at)
        update_at = create_at
        status = TaskStatus.NEW.value

        task = Task(
            task_id=task_id,
            status=status,
            type=type,
            task_detail=task_detail,
            create_user=user_id,
            create_at=create_at,
            update_at=update_at,
        )
        task.save()

        return jsonify(task.to_json()), 200

    except Exception as exception:
        return _gen_error_response(
            status_code=500,
            error_code=INTERNAL_SERVER_ERROR,
            message=f"ISLAM Exception: {str(exception)}",
        )
    
def change_tasks_status(request,s=""):
    """
    Request:
        headers:
        {
            
        }
        body:
        {
            "task_info":{
                "task_id": "123",
                "status": "NEW",
                "type" : "BASIC",
                "task_detail" : {},
                "create_user" : "",
                "create_at" : "",
                "update_at" : ""
            }
        }
    Returns:
        headers:
        {
            
        }
        body:
        {
            "task_info":{
                "task_id": "123",
                "status": "RUNNING",
                "type" : "BASIC",
                "task_detail" : {},
                "create_user" : "",
                "create_at" : "",
                "update_at" : ""
            }
        }
    """
    try:
        task_info = request.json.get("task_info")
        task_id = task_info.get("task_id")
        status = task_info.get("status")
        type = task_info.get("type")
        task_detail = task_info.get("task_detail")
        create_user = task_info.get("create_user")
        create_at = task_info.get("create_at")
        if(status==s):
            return _gen_error_response(
                status_code=400,
                error_code=MALEFORMED_REQUEST,
                message=f"Task status is {s} already",
            )
        if s not in [task_status.value for task_status in TaskStatus]:
            return _gen_error_response(
                status_code=400,
                error_code=MALEFORMED_REQUEST,
                message=f"Task status {s} is not supported",
            )
        for task_status in TaskStatus:
            if(s==""):
                return _gen_error_response(
                status_code=400,
                error_code=MALEFORMED_REQUEST,
                message=f"No status assigned",
                )
            elif(s==task_status.value):
                status = task_status.value
                break
        update_at = time.time()
        update_at = int(update_at)
        task = Task(
            task_id=task_id,
            status=status,
            type=type,
            task_detail=task_detail,
            create_user=create_user,
            create_at=create_at,
            update_at=update_at,
        )
        task.save()
        return jsonify(task.to_json()), 200

    except Exception as exception:
        return _gen_error_response(
            status_code=500,
            error_code=INTERNAL_SERVER_ERROR,
            message=f"ISLAM Exception: {str(exception)}",
        )

def change_tasks_type(request,s=""):
    """
    Request:
        headers:
        {
            
        }
        body:
        {
            "task_info":{
                "task_id": "123",
                "status": "NEW",
                "type" : "BASIC",
                "task_detail" : {},
                "create_user" : "",
                "create_at" : "",
                "update_at" : ""
            }
        }
    Returns:
        headers:
        {
            
        }
        body:
        {
            "task_info":{
                "task_id": "123",
                "status": "RUNNING",
                "type" : "BASIC",
                "task_detail" : {},
                "create_user" : "",
                "create_at" : "",
                "update_at" : ""
            }
        }
    """
    try:
        task_info = request.json.get("task_info")
        task_id = task_info.get("task_id")
        status = task_info.get("status")
        type = task_info.get("type")
        task_detail = task_info.get("task_detail")
        create_user = task_info.get("create_user")
        create_at = task_info.get("create_at")
        if(type == s):
            return _gen_error_response(
                status_code=400,
                error_code=MALEFORMED_REQUEST,
                message=f"Task type is {s} already",
            )
        if s not in [task_type.value for task_type in TaskType]:
            return _gen_error_response(
                status_code=400,
                error_code=MALEFORMED_REQUEST,
                message=f"Task type {s} is not supported",
            )
        for task_type in TaskType:
            if(s==""):
                return _gen_error_response(
                status_code=400,
                error_code=MALEFORMED_REQUEST,
                message=f"No type assigned",
                )
            elif(s==task_type.value):
                type = task_type.value
                break
        update_at = time.time()
        update_at = int(update_at)
        task = Task(
            task_id=task_id,
            status=status,
            type=type,
            task_detail=task_detail,
            create_user=create_user,
            create_at=create_at,
            update_at=update_at,
        )
        task.save()
        return jsonify(task.to_json()), 200

    except Exception as exception:
        return _gen_error_response(
            status_code=500,
            error_code=INTERNAL_SERVER_ERROR,
            message=f"ISLAM Exception: {str(exception)}",
        )

def get_tasks_from_status(s=""):
    """
    Returns:
        [Task]
    """
    status_assigned = ""
    for task_status in TaskStatus:
            if(s==""):
                return _gen_error_response(
                status_code=400,
                error_code=MALEFORMED_REQUEST,
                message=f"No status assigned",
                )
            elif(s==task_status.value):
                status_assigned = task_status.value
                break
    tasks = Task.objects(status=status_assigned)
    return [task.to_json() for task in tasks]

def get_tasks_from_type(s=""):
    """
    Returns:
        [Task]
    """
    type_assigned = ""
    for task_type in TaskType:
            if(s==""):
                return _gen_error_response(
                status_code=400,
                error_code=MALEFORMED_REQUEST,
                message=f"No type assigned",
                )
            elif(s==task_type.value):
                type_assigned = task_type.value
                break
    tasks = Task.objects(type=type_assigned)
    return [task.to_json() for task in tasks]