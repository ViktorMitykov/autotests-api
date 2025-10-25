from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExercisesRequestSchema, \
    ExerciseSchema, GetExerciseResponseSchema
from clients.users.users_schema import GetUserResponseSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет что ожидаемый и актуальный результат совпадает
    :param actual: ExerciseSchema :param expected: ExerciseSchema
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")
    assert_equal(actual.order_index, expected.order_index, "order_index")


def assert_create_exercises_response(response: CreateExerciseResponseSchema, request: CreateExercisesRequestSchema):
    """
    Функция проверяет что ответ на создание упражнения соответствует запросу
    :param response:
    :type response:
    :param request:
    :type request:
    :return:
    :rtype:
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")


def assert_get_exercise_response(actual: GetExerciseResponseSchema, expected: CreateExerciseResponseSchema):
    """
    Проверяет что ответ получения упражнения соответствует запросу.
    :param actual: Ответ от получения пользователя
    :param expected: Ответ от создания пользователя

    """
    assert_exercise(actual.exercise, expected.exercise)
