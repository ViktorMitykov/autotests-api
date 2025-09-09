from __future__ import annotations

from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict

from clients.files.files_client import File
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict
from clients.users.private_user_client import User


class Course(TypedDict):
    """
    Описание структуры курса.
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User

class GetCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение файла
    """
    userId: str


class CreateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла
    """
    title: str
    maxScore: int | None
    minScor: int | None
    description: str
    estimatedTime: str | None
    previewFileId: str
    createdByUserId: str

class CreateCourseResponseDict(TypedDict):
    """
    Описание структуры ответа создания курса.
    """
    course: Course


class UpdateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на редактирование файла
    """
    title: str | None
    maxScore: str | None
    minScore: str | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(ApiClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод для получения списка курсов
        :param query: Словарь с userId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/courses", params=query)

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Метод для создания курсов
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/courses", json=request)

    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        """
        Метод для создания курсов
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: Ответ от сервера в виде объекта json
        """
        response = self.create_course_api(request)
        return response.json()

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса
        :param course_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/courses/{course_id}")

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Метод обновления курса
        :param course_id: Идентификатор курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса
        :param course_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/courses/{course_id}")


def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(get_private_http_client(user))
