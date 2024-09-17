from core.database.connection import AsyncSession
from core.exceptions.exc import BadRequestException
import re
from fastapi import status


class Validate:

    @staticmethod
    async def validate(form_data: dict, db=None, record_id: int | None = None):
        errors = {}
        if hasattr(form_data, "create_validation"):
            errors = await form_data.create_validation(errors, db)
        elif hasattr(form_data, "update_validation"):
            errors = await form_data.update_validation(errors, db, record_id)
        elif hasattr(form_data, "custom_validation"): 
            errors = await form_data.custom_validation(errors, db, record_id)

        if errors != {}:
            raise BadRequestException(errors=errors)



def check_email_is_valid(input: str) -> bool:
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return email_pattern.match(input)


def error_handler(error_message: str, fied_name: str, errors):
    if fied_name in errors:
        errors[fied_name].append(error_message)
    else:
        errors[fied_name] = [error_message]


def transform_pydantic_errors(errors):
    transformed_errors = {}
    for error in errors:
        field_name = error['loc'][-1]
        transformed_errors[field_name] = error['msg']
    return {
        "errors": transformed_errors,
        "message": "Request failed",
        "code": status.HTTP_400_BAD_REQUEST
    }