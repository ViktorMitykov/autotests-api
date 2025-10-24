from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, GetCoursesQuerySchema, \
    GetCoursesResponseSchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_equal, assert_status_code
from tools.assertions.course import assert_update_course_response, assert_get_courses_response, \
    assert_create_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.courses
class TestCourses:
    def test_update_course(self, courses_client: CoursesClient, function_courses: CoursesFixture):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(course_id=function_courses.response.course.id, request=request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_courses(self, courses_client: CoursesClient, function_user: UserFixture, function_courses: CoursesFixture):
        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)
        response = courses_client.get_courses_api(query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_courses.response])

        validate_json_schema(response.json(), response_data.model_json_schema())

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