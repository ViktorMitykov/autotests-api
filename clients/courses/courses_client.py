from __future__ import annotations
from clients.api_client import ApiClient
from httpx import Response
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.courses.courses_schema import GetCoursesQuerySchema, CreateCourseRequestSchema, CreateCourseResponseSchema, UpdateCourseRequestSchema

class CoursesClient(ApiClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод для получения списка курсов
        :param query: Словарь с userId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/courses",
                        params=query.model_dump(by_alias=True))

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод для создания курсов
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/courses",
                         json=request.model_dump(by_alias=True))

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Метод для создания курсов
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: Ответ от сервера в виде объекта json
        """
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса
        :param course_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/courses/{course_id}")

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод обновления курса
        :param course_id: Идентификатор курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/courses/{course_id}",
                          json=request.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса
        :param course_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/courses/{course_id}")


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(get_private_http_client(user))
