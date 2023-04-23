import json
from flask import Blueprint, Response, request
from service import user_service

from celery import shared_task
from celery.result import AsyncResult

@shared_task(ignore_result=False)
def add_together(a: int, b: int) -> int:
    return a + b

test_route = Blueprint("test_route", __name__)

@test_route.route("/", methods=["GET"])
def get_test():
    return "Hello ISLAM", 200

# start task
@test_route.route("/start", methods=["GET"])
def start_add() -> dict[str, object]:
    a = 1
    b = 2
    result = add_together.delay(a, b)
    return {"result_id": result.id}

# get task result
@test_route.route("/result/<id>")
def task_result(id: str) -> dict[str, object]:
    result = AsyncResult(id)
    return Response(json.dumps({
        "ready": result.ready(),
        "successful": result.successful(),
        "value": result.result if result.ready() else None,
    }), mimetype='application/json')