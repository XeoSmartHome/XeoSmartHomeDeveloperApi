from flask import Request, json
from werkzeug.exceptions import BadRequest

APPLICATION_JSON = 'application/json'
MULTIPART_FORM_DATA = 'multipart/form-data'


class RequestParser:
    def __init__(self, request: Request):
        """
        Parse the request to extract arguments from it.
        :param request: Request, a flask request
        """

        if request.method == 'GET':
            self._data = request.args

        elif request.method == 'POST':
            content_type = request.headers.get('Content-Type')

            if content_type == APPLICATION_JSON:
                self._data = json.loads(request.data.decode('utf-8'))

            elif content_type == MULTIPART_FORM_DATA:
                self._data = request.form

            else:
                raise BadRequest('UnknownContentType')

    def get_arg(self, key: str, data_type: type = None, required: bool = True):
        """
        Extract an argument from the request. By default raise error if argument is not found.
        :param key: str, key of the argument
        :param data_type: type, expected data type for the argument
        :param required: bool, True if argument can not by None, else False, Default True
        :return: any
        """
        arg = self._data.get(key)

        if arg is None and required is True:
            raise BadRequest('ArgNotFound')

        if data_type is not None and type(arg) != data_type:
            try:
                arg = data_type(arg)
            except ValueError:
                raise BadRequest()

        return arg
