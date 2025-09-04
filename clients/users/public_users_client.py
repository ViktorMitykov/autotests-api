from clients.api_client import ApiClient
from typing import TypedDict
from httpx import Response

class CreateRequestUserDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    midleName: str

class PublicusersClient(ApiClient):
    def create_user_api(self, request: CreateRequestUserDict) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с email, password, lastName, firstName, midleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/users", json=request)