from flask import Blueprint, request
from service import user_service

test_route = Blueprint("test_route", __name__)


@test_route.route("/", methods=["GET"])
def get_test():
    return "Hello ISLAM", 200