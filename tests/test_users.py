from clients.users.private_user_client import PrivateUserClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake
import pytest

@pytest.mark.regression
@pytest.mark.users
class TestUser:
    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
    def test_create_user(self, domain: str, public_user_client: PublicUsersClient):
        request = CreateUserRequestSchema(email=fake.email(domain=domain))
        response = public_user_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_user_me(self, function_user, private_user_client: PrivateUserClient):
        response = private_user_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)
        validate_json_schema(response.json(), response_data.model_json_schema())
