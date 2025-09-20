from clients.users.public_users_client import get_public_user_client
from clients.authentication.authentication_client import get_authentication_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from tools.assertions.aunthentication import assert_login_response
from tools.assertions.base import assert_status_code
from http import HTTPStatus
from jsonschema import validate


def test_login():
    public_users_client = get_public_user_client()
    auth_client = get_authentication_client()

    create_user_request = CreateUserRequestSchema()
    public_users_client.create_user(create_user_request)

    login_request = LoginRequestSchema(email=create_user_request.email, password=create_user_request.password)
    login_response = auth_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)
    validate(instance=login_response.json(), schema=LoginResponseSchema.model_json_schema())
