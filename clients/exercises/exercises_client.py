from __future__ import annotations

from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict

class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса для получения курсов
    """
    courseId: str

class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]

class GetExerciseResponseDict(TypedDict):
    exercise: Exercise

class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса для создание курса
    """
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None

class CreateExerciseResponseDict(TypedDict):
    exercise: Exercise

class UpdateExerciseRequestApi(TypedDict):
    """
    Описание структуры запроса для обновления курса
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(ApiClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения курсов
        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/exercises", params=query)

    def get_exrcises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод получения курсов
        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта json
        """
        response = self.get_exercises_api(query)
        return response.json()


    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения курса
        :param exercise_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод получения курса
        :param exercise_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта json
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод создания курса
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/exercises", json=request)

    def create_exercise(self, request: CreateExercisesRequestDict) -> CreateExerciseResponseDict:
        """
        Метод создания курса
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта json
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise_api(self, request: UpdateExerciseRequestApi) -> Response:
        """
        Метод обновления курса
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url="/api/v1/exercises/{exercise_id}", json=request)

    def update_exercise(self, request: UpdateExerciseRequestApi):
        """
        Метод обновления курса
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта json
        """
        response = self.update_exercise_api(request)
        return response.json()

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления курса
        :param exercise_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/exercises/{exercise_id}")

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))

