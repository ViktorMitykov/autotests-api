from __future__ import annotations

from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict

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
    minScor: str | None
    description: str
    estimatedTime: str | None
    previewFileId: str
    createdByUserId:str

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

