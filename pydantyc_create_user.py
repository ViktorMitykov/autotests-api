from pydantic import BaseModel, EmailStr, Field

"""
Думал еще вот такой класс сделать, чтобы от него наследоваться и не дублировать поля, 
    не знаю насколько жизнеспособно, если пояснишь, было бы здорово!
    
class UserNameScheme(BaseModel):
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
"""

class UserScheme(BaseModel):
    """
    Описание структуры юзера
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestScheme(BaseModel):
    """
    Описание структуры запроса на создание юзера
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseScheme(BaseModel):
    """
    Описание структуры ответа на создание юзера
    """
    user: UserScheme