from flask import Blueprint, request
from service import task_service

task_route = Blueprint("query_route", __name__)