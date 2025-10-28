import allure
from allure_commons.types import Severity

from clients.users.private_user_client import PrivateUserClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus

from fixtures.users import UserFixture
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake
import pytest


@pytest.mark.regression
@pytest.mark.users
@allure.tag(AllureTag.REGRESSION, AllureTag.EXERCISES)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
@allure.suite(AllureFeature.USERS)
class TestUser:
    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
    @allure.title("Create user")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_create_user(self, domain: str, public_user_client: PublicUsersClient):
        request = CreateUserRequestSchema(email=fake.email(domain))
        response = public_user_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get user me")
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_get_user_me(self, function_user: UserFixture, private_user_client: PrivateUserClient):
        response = private_user_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)
        validate_json_schema(response.json(), response_data.model_json_schema())