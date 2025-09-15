from __future__ import annotations

from clients.api_client import ApiClient
from httpx import Response
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.exercises.exercises_schema import GetExerciseQuerySchema, GetExerciseResponseSchema, CreateExercisesRequestSchema, CreateExerciseResponseSchema, UpdateExerciseRequestApiSchema, UpdateExerciseResponseApiSchema


class ExercisesClient(ApiClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExerciseQuerySchema) -> Response:
        """
        Метод получения курсов
        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/exercises",
                        params=query.model_dump(by_alias=True))

    def get_exrcises(self, query: GetExerciseQuerySchema) -> GetExerciseResponseSchema:
        """
        Метод получения курсов
        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта json
        """
        response = self.get_exercises_api(query)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения курса
        :param exercise_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод получения курса
        :param exercise_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта json
        """
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise_api(self, request: CreateExercisesRequestSchema) -> Response:
        """
        Метод создания курса
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/exercises",
                         json=request.model_dump(by_alias=True))

    def create_exercise(self, request: CreateExercisesRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод создания курса
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта json
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise_api(self, request: UpdateExerciseRequestApiSchema) -> Response:
        """
        Метод обновления курса
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url="/api/v1/exercises/{exercise_id}",
                          json=request.model_dump(by_alias=True))

    def update_exercise(self, request: UpdateExerciseRequestApiSchema) -> UpdateExerciseResponseApiSchema:
        """
        Метод обновления курса
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта json
        """
        response = self.update_exercise_api(request)
        return UpdateExerciseResponseApiSchema.model_validate_json(response.text)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления курса
        :param exercise_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/exercises/{exercise_id}")

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))

