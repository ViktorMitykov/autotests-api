from tools.assertions.base import assert_equal
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema, \
    UserSchema


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


def assert_user(expected: UserSchema, actual: UserSchema):
    """
    Проверяет, что ожидаемый и актуальный результат совпадает.

    :param actual: UserSchema
    :param expected: UserSchema
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(expected.id, actual.id, "id")
    assert_equal(expected.email, actual.email, "email")
    assert_equal(expected.last_name, actual.last_name, "last_name")
    assert_equal(expected.first_name, actual.first_name, "first_name")
    assert_equal(expected.middle_name, actual.middle_name, "middle_name")


def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """
    Проверяет что ответ получения пользователя соответствует запросу.

    :param get_user_response: Ответ от метода получения пользователя
    :param create_user_response: Ответ от метода создания пользователя
    """
    assert_user(get_user_response.user, create_user_response.user)

