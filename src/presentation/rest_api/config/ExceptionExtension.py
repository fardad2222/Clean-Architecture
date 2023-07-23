from werkzeug.exceptions import HTTPException


def handle_global_error(error: HTTPException):
    """ Make Json Error Response instead of web page """
    response = {
        'error': error.__class__.__name__,
        'message': error.description
    }
    return response, error.code


def register_exception_handler(app):
    app.register_error_handler(HTTPException, handle_global_error)
