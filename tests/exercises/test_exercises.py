from http import HTTPStatus
import pytest
from httpx import request

from clients.errors_schema import IternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExercisesRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, UpdateExerciseRequestApiSchema, UpdateExerciseResponseApiSchema
from fixtures.courses import CoursesFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercises_response, assert_get_exercise_response, \
    asser_update_exercise_response, assert_exercise_not_found_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(self, exercises_client: ExercisesClient, function_courses: CoursesFixture):
        request = CreateExercisesRequestSchema(course_id=function_courses.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercises_response(response_data, request)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercise(self, exercises_client: ExercisesClient, function_exercises: ExerciseFixture):
        response = exercises_client.get_exercise_api(function_exercises.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercises.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_update_exercise(self, exercises_client: ExercisesClient, function_exercises: ExerciseFixture):
        request = UpdateExerciseRequestApiSchema()
        response = exercises_client.update_exercise_api(function_exercises.response.exercise.id, request)
        response_data = UpdateExerciseResponseApiSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        asser_update_exercise_response(response_data, request)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_delete_exercise(self, exercises_client: ExercisesClient, function_exercises: ExerciseFixture):
        response = exercises_client.delete_exercise_api(function_exercises.response.exercise.id)
        assert_status_code(response.status_code, HTTPStatus.OK)

        get_response = exercises_client.get_exercise_api(function_exercises.response.exercise.id)
        get_response_data = IternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(get_response_data)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

