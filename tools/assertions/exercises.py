from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExercisesRequestSchema
from tools.assertions.base import assert_equal

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