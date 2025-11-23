import allure
from httpx import Response

from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.routes import ApiRoutes
from clients.api_coverage import tracker


class PublicUsersClient(ApiClient):
    @allure.step("Create user")
    @tracker.track_coverage_httpx(f"{ApiRoutes.USERS}")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с email, password, lastName, firstName, midleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=f"{ApiRoutes.USERS}",
                         json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с email, password, lastName, firstName, midleName
        :return: Ответ от сервера в виде объекта json
        """
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_user_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(get_public_http_client())
