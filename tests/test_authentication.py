import pytest
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from tests.conftest import UserFixture
from tools.assertions.aunthentication import assert_login_response
from tools.assertions.base import assert_status_code
from http import HTTPStatus
from jsonschema import validate

@pytest.mark.regression
@pytest.mark.authentication
def test_login(authentication_client: AuthenticationClient, function_user: UserFixture):
    request = LoginRequestSchema(email=function_user.email, password=function_user.password)
    response = authentication_client.login_api(request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)
    validate(instance=response.json(), schema=LoginResponseSchema.model_json_schema())
