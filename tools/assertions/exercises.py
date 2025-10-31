import allure

from clients.errors_schema import IternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExercisesRequestSchema, \
    ExerciseSchema, GetExerciseResponseSchema, UpdateExerciseRequestApiSchema, UpdateExerciseResponseApiSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_iternal_error_response


@allure.step("Check exercise")
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
    assert_equal(actual.estimated_time, expected.estimated_time,
                 "estimated_time")
    assert_equal(actual.order_index, expected.order_index, "order_index")


@allure.step("Check create exercise response")
def assert_create_exercises_response(response: CreateExerciseResponseSchema,
                                     request: CreateExercisesRequestSchema):
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
    assert_equal(response.exercise.order_index, request.order_index,
                 "order_index")
    assert_equal(response.exercise.description, request.description,
                 "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time,
                 "estimated_time")


@allure.step("Check get exercise response")
def assert_get_exercise_response(actual: GetExerciseResponseSchema,
                                 expected: CreateExerciseResponseSchema):
    """
    Проверяет что ответ получения упражнения соответствует запросу.
    :param actual: Ответ от получения пользователя
    :param expected: Ответ от создания пользователя

    """
    assert_exercise(actual.exercise, expected.exercise)


@allure.step("Check update exercise response")
def asser_update_exercise_response(actual: UpdateExerciseResponseApiSchema,
                                   expected: UpdateExerciseRequestApiSchema):
    """
    Проверяет что ответ на обновление задания соответствует запросу
    :param actual: UpdateExerciseResponseApiSchema
    :param expected: UpdateExerciseRequestApiSchema
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.description, expected.description,
                 "description")
    assert_equal(actual.exercise.order_index, expected.order_index,
                 "order_index")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time,
                 "estimated_time")


@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: IternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если задание не найдено на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    expected = IternalErrorResponseSchema(details="Exercise not found")
    assert_iternal_error_response(actual, expected)


@allure.step("Check get exercise response")
def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_response: list[CreateExerciseResponseSchema]):
    """
    Проверяет, что ответ на получение списка курсов соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе списка курсов.
    :param  create_exercise_response: Список API ответов при создании курсов.
    :raises AssertionError: Если данные курсов не совпадают.
    """
    assert_length(get_exercises_response.exercises, create_exercise_response,
                  "exercises")

    for index, create_exercise_response in enumerate(create_exercise_response):
        assert_exercise(get_exercises_response.exercises[index],
                        create_exercise_response.exercise)
