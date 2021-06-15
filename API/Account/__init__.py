from flask import request
from flask_login import login_user

from Repos import developers_repo
from RequestParser import RequestParser
from Services import developers_service
from ..blueprint import api


@api.post('/login')
def handle_login():
    """
    * Method: POST
    """

    request_parser = RequestParser(request)

    email = request_parser.get_arg('emailAddress')
    password = request_parser.get_arg('password')

    developer = developers_repo.get_developer_by_email(email)

    if not developer.check_password(password):
        return ''

    login_user(developer)

    return {'ok': 'ok'}


@api.post('/create-account')
def handle_create_account():
    """
    * Methods: POST
    """

    request_parser = RequestParser(request)

    first_name = request_parser.get_arg('firstName')
    last_name = request_parser.get_arg('lastName')
    email_address = request_parser.get_arg('emailAddress')
    password = request_parser.get_arg('password')
    phone_number = request_parser.get_arg('phoneNumber')

    new_developer = developers_service.create_developer(first_name, last_name, email_address, password, phone_number)

    login_user(new_developer)

    return 'ok'
