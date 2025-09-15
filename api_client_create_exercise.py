from clients.courses.courses_client import get_courses_client
from clients.exercises.exercises_client import get_exercises_client
from clients.files.files_client import get_files_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_user_client
from tools.fakers import get_random_email
from clients.users.users_schema import CreateUserRequestSchema
from clients.files.files_schema import CreateFileRequestSchema
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_schema import CreateExercisesRequestSchema

public_user_client = get_public_user_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string")

create_user_response = public_user_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_course_request = CreateCourseRequestSchema(
    title="Api Course",
    maxScore=100,
    minScore=10,
    description="Python api course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)

create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

exercises_client = get_exercises_client(authentication_user)
create_exercise_request = CreateExercisesRequestSchema(
    title="Test course",
    courseId=create_course_response.course.id,
    maxScore=100,
    minScore=10,
    orderIndex=50,
    description="Test course description",
    estimatedTime="2 week")

create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print("Create exercise data:", create_exercise_response)