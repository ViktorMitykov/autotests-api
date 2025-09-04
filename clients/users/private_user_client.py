from __future__ import annotations

from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict

class UpdateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление пользователя
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

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

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Метод обновления юзера по идентификатору.
        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления юзера по идентификатору
        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/users/{user_id}")