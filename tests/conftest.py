import pytest
from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.users.public_users_client import get_public_user_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema
from pydantic import BaseModel, EmailStr
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_user_client import get_private_user_client, PrivateUserClient


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema
    authentication_user: AuthenticationUserSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()


@pytest.fixture
def public_user_client() -> PublicUsersClient:
    return get_public_user_client()


@pytest.fixture()
def function_user(public_user_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request)
    authentication_user = AuthenticationUserSchema(email=request.email, password=request.password)
    return UserFixture(request=request, response=response, authentication_user=authentication_user)


@pytest.fixture()
def private_user_client(function_user: UserFixture) -> PrivateUserClient:
    return get_private_user_client(function_user.authentication_user)



