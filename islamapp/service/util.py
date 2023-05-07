from flask import Response
from schema.util import ErrorResponseSchema
import random
import string

INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
USER_NOT_FOUND = "USER_NOT_FOUND"
DUPLICATE_REGISTRATION = "DUPLICATE_REGISTRATION"
MALEFORMED_REQUEST = "MALEFORMED_REQUEST"
TASK_NOT_FOUND = "TASK_NOT_FOUND"
INVALID_INPUT_ERROR = "INVALID_INPUT_ERROR"
RETRY_ERROR = "RETRY_ERROR"

def _gen_error_response(status_code=None, error_code=None, message=None):
    return Response(
        ErrorResponseSchema(
            error_code=error_code,
            message=message,
        ).json(),
        status=status_code,
        mimetype="text/json",
    )

def _gen_user_id():
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits
    user_id = ''
    first_section = ''.join(random.choices(characters, k=5))+'-'
    second_section = ''.join(random.choices(characters, k=10))+'-'
    third_section = ''.join(random.choices(characters, k=15))
    user_id = first_section + second_section + third_section
    return user_id