from datetime import datetime

from typing_extensions import Annotated

from app.models.user import UserRole
from pydantic import BaseModel, Field


class UserCreateSchema(BaseModel):
    password: Annotated[str, Field(max_length=50)]
    first_name: Annotated[str, Field(max_length=50)]
    last_name: Annotated[str, Field(max_length=50)]
    patronymic: Annotated[str, Field(max_length=50)]
    birth_date: datetime
    country: Annotated[str, Field(max_length=50)]
    city: Annotated[str, Field(max_length=50)]
    phone: Annotated[str, Field(max_length=50)]
    email: Annotated[str, Field(max_length=50)]
    role: UserRole
