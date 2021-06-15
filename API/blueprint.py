from flask import Blueprint

api = Blueprint('api', __name__, template_folder='templates', static_folder='static')


@api.errorhandler(AssertionError)
def handle_assertion_exception(error):
    return {'error': 'AssertionException'}


@api.errorhandler(Exception)
def handle_exception(error):
    print(error)
    return {'error': 'GenericException'}
