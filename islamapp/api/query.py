from flask import Blueprint, request
from service import query_service

query_route = Blueprint("query_route", __name__)

@query_route.route("/api/v1/islam/query", methods=["POST"])
def query():
    return query_service.query(request)