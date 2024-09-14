from pydantic import BaseModel
from typing import Generic, TypeVar
from core.database.connection import Base


ModelType = TypeVar("ModelType", bound=Base)
SchemaType = TypeVar("SchemaType", bound=BaseModel)


class SuccessResponse(BaseModel, Generic[SchemaType]):
    code: int = 200
    message: str
    data: SchemaType | dict[str, list[SchemaType] | int]

    @staticmethod
    def show(
        *, data: ModelType, message: str = "success", code: int = 200
    ):
        return {
            "data": data,
            "message": message,
            "code": code,
        }