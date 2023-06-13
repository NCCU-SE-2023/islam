import requests
import os
import dotenv

dotenv.load_dotenv()

SELENIUM_GRID_HUB_ENDPOINT = os.environ.get("SELENIUM_GRID_HUB_ENDPOINT")
SELENIUM_GRID_GRAPHQL_END_POINT = os.getenv("SELENIUM_GRID_GRAPHQL_END_POINT")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")


def log_while_exception():
    # This decorator will print the function name when it throws an exception.
    def function_wrapper(func):
        def caller(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as exception:
                print(f"'{func.__name__}' throw an exception.")
                raise exception

        return caller

    return function_wrapper


def grid_get_node_count(SELENIUM_GRID_GRAPHQL_END_POINT) -> int:
    url = SELENIUM_GRID_GRAPHQL_END_POINT
    body = {"query": "{grid {nodeCount}}"}
    response = requests.post(url, json=body)
    return response.json()["data"]["grid"]["nodeCount"]


def grid_get_ndoe_status(SELENIUM_GRID_GRAPHQL_END_POINT) -> list:
    url = SELENIUM_GRID_GRAPHQL_END_POINT
    body = {"query": "{ nodesInfo { nodes { status, id, maxSession, sessionCount} } }"}
    response = requests.post(url, json=body)
    return response.json()["data"]["nodesInfo"]["nodes"]
