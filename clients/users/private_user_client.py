from __future__ import annotations

from clients.api_client import ApiClient
from httpx import Response
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import GetUserResponseSchema, UpdateUserRequestSchema


class PrivateUserClient(ApiClient):
    """
    Клиент для работы с /api/v1/users
    """
    def get_user_me_api(self) -> Response:
        """
        Метод получения текущего юзера
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения юзера по идентификатору
        :param user_id: Индентификатор
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Метод получения юзера по идентификатору
        :param user_id: Индентификатор
        :return: Ответ от сервера в виде объекта json
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод обновления юзера по идентификатору.
        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/users/{user_id}",
                          json=request.model_dump(by_alias=True))

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления юзера по идентификатору
        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/users/{user_id}")

def get_private_user_client(user: AuthenticationUserSchema) -> PrivateUserClient:
    """
   Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

   :return: Готовый к использованию PrivateUsersClient.
   """
    return PrivateUserClient(get_private_http_client(user))