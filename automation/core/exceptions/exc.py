from core.exceptions.base import CustomException
from fastapi import status



class NotFoundException(CustomException):
    message = "Item not found"
    status_code = status.HTTP_404_NOT_FOUND
    def __init__(self, message=None, status_code=None):
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code


class AuthFailedException(CustomException):
    message = "Invalid credentials"
    status_code = status.HTTP_401_UNAUTHORIZED


class BadRequestException(CustomException):
    message = "Request failed"
    status_code = status.HTTP_400_BAD_REQUEST
    def __init__(self, message=None, status_code=None, errors=None):
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code
        if errors:
            self.errors = errors


class ProccessFailedException(CustomException):
    message = "proccess failed"
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    def __init__(self, message=None, status_code=None):
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code