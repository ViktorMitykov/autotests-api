import allure

from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, IternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.logger import get_logger

logger = get_logger("ERRORS_ASSERTIONS")


@allure.step("Check validate error")
def assert_validation_error(actual: ValidationErrorSchema,
                            expected: ValidationErrorSchema):
    """
    Проверяет, что объект ошибки валидации соответствует ожидаемому значению.

    :param actual: Фактическая ошибка.
    :param expected: Ожидаемая ошибка.
    :raises AssertionError: Если значения полей не совпадают.
    """
    logger.info("Check validate error")
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.location, expected.location, "location")


@allure.step("Check validate error response")
def assert_validation_error_response(actual: ValidationErrorResponseSchema,
                                     expected: ValidationErrorResponseSchema):
    """
    Проверяет, что объект ответа API с ошибками валидации (`ValidationErrorResponseSchema`)
    соответствует ожидаемому значению.

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_length(actual.details, expected.details, "details")

    for index, detail in enumerate(expected.details):
        logger.info("Check validate error")
        assert_validation_error(actual.details[index], detail)


@allure.step("Check iternal error response")
def assert_iternal_error_response(actual: IternalErrorResponseSchema,
                                  expected: IternalErrorResponseSchema):
    """
    Функция для проверки внутренней ошибки. Например, ошибки 404 (File not found).

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    logger.info("Check iternal error response")
    assert_equal(actual.details, expected.details, "details")
