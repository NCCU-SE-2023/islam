import json
import time
from flask import Blueprint, Response, request
from service import user_service

from celery import shared_task
from celery.result import AsyncResult
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task(
    ignore_result=False,
    name="tasks.add",
    max_retries=3,
    default_retry_delay=10,
    time_limit=int(60 * 60 * 24 * 7),
    # backend="redis://localhost:6379/0",
    # broker="redis://localhost:6379/0",
    bind=True, # use this if the task is a method of the class
)
def add_together(self,a: int, b: int) -> int:
    self.update_state(state='PROGRESS',meta={'current': 2, 'total': 4})
    logger.info("Adding {0} + {1}".format(a, b))
    # sleep 30 seconds
    time.sleep(30)
    # run a while that loop 200000 times
    for i in range(2000000000000000000):
        print(i)
    return a + b

'''
# chain of tasks
def update_page_info(url):
    # fetch_page -> parse_page -> store_page
    chain = fetch_page.s(url) | parse_page.s() | store_page_info.s(url)
    chain()

@app.task()
def fetch_page(url):
    return myhttplib.get(url)

@app.task()
def parse_page(page):
    return myparser.parse_document(page)

@app.task(ignore_result=True)
def store_page_info(info, url):
    PageInfo.objects.create(url=url, info=info)
'''

celery_route = Blueprint("celery_route", __name__)


# start task
@celery_route.route("/start", methods=["GET"])
def start_add() -> dict[str, object]:
    a = 1
    b = 2
    result = add_together.delay(a, b)
    return {"result_id": result.id}


# get task result
@celery_route.route("/result/<id>")
def task_result(id: str) -> dict[str, object]:
    result = AsyncResult(id)
    return Response(
        json.dumps(
            {
                "ready": result.ready(),
                "successful": result.successful(),
                "value": result.result if result.ready() else None,
            }
        ),
        mimetype="application/json",
    )


