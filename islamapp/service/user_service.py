from database import db
from model.user import User
from service.util import (
    _gen_error_response,
    _gen_user_id,
    DUPLICATE_REGISTRATION,
    INTERNAL_SERVER_ERROR,
    USER_NOT_FOUND,
    INVALID_INPUT_ERROR
)

from flask import jsonify

def post_user(request):
    '''
    Requests:
        body:
        {
            "account": "string",
            "password": "string"
        }
    Returns:
        headers:
        {
            "user_id": "string",
        }
        body:
        {
            "account": "string",
        }
    '''
    try:
        account = request.json.get('account')
        password = request.json.get('password')

        user = User.query.filter_by(account=account).first()
        if user is not None:
            return _gen_error_response(
                status_code=409,
                error_code=DUPLICATE_REGISTRATION,
                message="User already exist",
            )
        
        user_id = _gen_user_id()
        user = User(user_id=user_id, account=account, password=password)
        db.session.add(user)
        db.session.commit()

        user = user.to_json()
        user.pop('user_id')
        user = jsonify(user)
        user.headers.add("user_id",user_id)

        return user, 200

    except Exception as exception:
        return _gen_error_response(
            status_code=500,
            error_code=INTERNAL_SERVER_ERROR,
            message=f"ShyGuy Exception: {str(exception)}",
        )

def get_user(request):
    try:
        account = request.json.get('account')
        password = request.json.get('password')
        user = User.query.filter_by(account=account, password=password).first()
        if user is None:
            return _gen_error_response(
                status_code=404,
                error_code=USER_NOT_FOUND,
                message="User not found",
            )
        
        user = user.to_json()
        user_id = user.get('user_id')
        user.pop('user_id')
        user = jsonify(user)
        user.headers.add("user_id", user_id)

        return user, 200

    except Exception as exception:
        return _gen_error_response(
            status_code=500,
            error_code=INTERNAL_SERVER_ERROR,
            message=f"ShyGuy Exception: {str(exception)}",
        )

def get_user_by_id(request):
    try:
        user_id = request.headers.get('user_id')
        user = User.query.filter_by(user_id=user_id).first()
        if user is None:
            return _gen_error_response(
                status_code=404,
                error_code=USER_NOT_FOUND,
                message="User not found",
            )
        
        user = user.to_json()
        user_id = user.get('user_id')
        user.pop('user_id')
        user = jsonify(user)
        user.headers.add("user_id", user_id)

        return user, 200

    except Exception as exception:
        return _gen_error_response(
            status_code=500,
            error_code=INTERNAL_SERVER_ERROR,
            message=f"ShyGuy Exception: {str(exception)}",
        )
    
def insert_cookie(request):
    try:
        userid = request.json.get('user_id')
        cookie = request.json.get('cookie')
        user = User.query.filter_by(user_id=userid).first()
        if user is None:
            return _gen_error_response(
                status_code=404,
                error_code=USER_NOT_FOUND,
                message="User not found",
            )
        success = User.query.filter_by(user_id=userid).update({'cookie' : cookie})
        if success == 0:
            return _gen_error_response(
                status_code=400,
                error_code=INVALID_INPUT_ERROR,
                message="Bad cookie input",
            )
        db.session.commit()
        user = User.query.filter_by(user_id=userid).first()
        user = jsonify(user.to_json())
        return user, 200
    except Exception as exception:
        if(exception.__class__.__name__=="BadRequest"):
            return _gen_error_response(
            status_code=400,
                error_code=INVALID_INPUT_ERROR,
                message="Bad cookie input",
        )
        return _gen_error_response(
            status_code=500,
            error_code=INTERNAL_SERVER_ERROR,
            message=f"ShyGuy Exception: {str(exception)}",
        )
