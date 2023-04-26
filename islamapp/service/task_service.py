from model.task import Task
from service.util import (
    _gen_error_response,
    INTERNAL_SERVER_ERROR,
    MALEFORMED_REQUEST,
)
import time
from flask import jsonify
from model.task import Task, TaskException



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

        task = Task.create_task(
            user_id=user_id,
            type=type,
            task_detail=task_detail,
        )

        return jsonify(task.to_json()), 201

    except TaskException as exception:
        return _gen_error_response(
            status_code=500,
            error_code=INTERNAL_SERVER_ERROR,
            message=f"ISLAM Exception: {str(exception)}",
        )
    except Exception as exception:
        return _gen_error_response(
            status_code=500,
            error_code=INTERNAL_SERVER_ERROR,
            message=f"ISLAM Exception: {str(exception)}",
        )

def get_task(request):
    """
    Request:
        headers:
        {
            "user_id": "dummy-user-id"
        }
    Returns:
        headers:
        {
            "user_id": "dummy-user-id"
        }
        body:
        {
            "tasks":[
                
            ]
        }
    """
    try:
        user_id = request.headers.get("user_id")

        tasks = Task.get_by_create_user(user_id)
        response = {
            "tasks": [task.to_json() for task in tasks]
        }

        return jsonify(response), 200
    except Exception as exception:
        return _gen_error_response(
            status_code=500,
            error_code=INTERNAL_SERVER_ERROR,
            message=f"ISLAM Exception: {str(exception)}",
        )

def update_task(request):
    """
    Request:
        headers:
        {
            "task_id": "dummy-task-id"
        }
        body:
        {
            "status": "RUNNING",
            "error_msg": {},
            "retry" : "True"
        }
    Returns:
        headers:
        {
            "task_id": "dummy-task-id"
        }
        body:
        {
            "task_id": "",
            "status": "",
            ...    
            
        }
    """
    try:
        task_id = request.headers.get("task_id")
        task = Task.objects(task_id=task_id)
        status = request.body.get("status")
        error_msg = request.body.get("error_msg")
        retry = request.body.get("retry")
        if status is not None:
            task.set_status(status)
        if error_msg is not None:
            task.set_errmsg(error_msg)
        if retry is not None and retry == "True":
            task.retry_task()

        return jsonify(task.to_json()), 201
    
    except TaskException as exception:
        return _gen_error_response(
            status_code=500,
            error_code=INTERNAL_SERVER_ERROR,
            message=f"ISLAM Exception: {str(exception)}",
        )
    
