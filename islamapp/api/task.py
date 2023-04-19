from flask import Blueprint, request
from service import task_service

task_route = Blueprint("task_route", __name__)


@task_route.route("/api/v1/islam/task", methods=["POST"])
def new_task():
    return task_service.new_task(request)