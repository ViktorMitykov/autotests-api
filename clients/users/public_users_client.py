from clients.api_client import ApiClient
from typing import TypedDict
from httpx import Response
from clients.public_http_builder import get_public_http_client

class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    midleName: str

class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: User

class CreateRequestUserDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(ApiClient):
    def create_user_api(self, request: CreateRequestUserDict) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с email, password, lastName, firstName, midleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/users", json=request)

    def create_user(self, request: CreateRequestUserDict) -> CreateUserResponseDict:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с email, password, lastName, firstName, midleName
        :return: Ответ от сервера в виде объекта json
        """
        response = self.create_user_api(request).json()
        return response

def get_public_user_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(get_public_http_client())