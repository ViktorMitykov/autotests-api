from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UserSchema(BaseModel):
    """
    Описание структуры юзера
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя
    """
    model_config = ConfigDict(populate_by_name=True)
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание пользователя
    """
    user: UserSchema

class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение пользователя
    """
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя
    """
    model_config = ConfigDict(populate_by_name=True)
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления пользователя.
    """
    user: UserSchema







