from http import HTTPStatus

import pytest
import allure
from allure_commons.types import Severity

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, GetCoursesQuerySchema, \
    GetCoursesResponseSchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.base import assert_equal, assert_status_code
from tools.assertions.course import assert_update_course_response, assert_get_courses_response, \
    assert_create_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.courses
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.suite(AllureFeature.COURSES)
class TestCourses:
    @allure.title("Update course")
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_update_course(self, courses_client: CoursesClient, function_courses: CoursesFixture):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(course_id=function_courses.response.course.id, request=request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get course")
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    @allure.severity(Severity.NORMAL)
    def test_get_courses(self, courses_client: CoursesClient, function_user: UserFixture, function_courses: CoursesFixture):
        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)
        response = courses_client.get_courses_api(query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_courses.response])

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Create course")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_create_course(self, courses_client: CoursesClient, function_user: UserFixture, function_file: FileFixture):
        request = CreateCourseRequestSchema(
            preview_file_id=function_file.response.file.id,
            created_by_user_id=function_user.response.user.id
        )
        response = courses_client.create_course_api(request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(response_data, request)

        validate_json_schema(response.json(), response_data.model_json_schema())