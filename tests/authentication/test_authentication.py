import allure
from allure_commons.types import Severity
import pytest
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture
from tools.allure.tags import AllureTag
from tools.assertions.aunthentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from http import HTTPStatus
from jsonschema import validate


@pytest.mark.regression
@pytest.mark.authentication
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHENTICATION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.suite(AllureFeature.AUTHENTICATION)
class TestAuthntication:
    @allure.title("Login")
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.LOGIN)
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.LOGIN)
    def test_login(self, authentication_client: AuthenticationClient, function_user: UserFixture):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)
        validate(instance=response.json(), schema=LoginResponseSchema.model_json_schema())