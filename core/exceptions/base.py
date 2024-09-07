from fastapi import HTTPException, status


class CustomException(HTTPException):
    message = ""
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    errors = {}
    def __init__(self, message = None, status_code = None,  errors = None, headers = None):
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code
        if errors:
            self.errors = errors
        if headers:
            self.headers = headers
