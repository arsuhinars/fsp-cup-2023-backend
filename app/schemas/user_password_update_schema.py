from pydantic import BaseModel

from app.schemas.user_create_schema import PasswordField


class UserPasswordUpdateSchema(BaseModel):
    new_password: PasswordField
