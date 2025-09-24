import pytest
from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.users.public_users_client import get_public_user_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema
from pydantic import BaseModel, EmailStr


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

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
    return UserFixture(request=request, response=response)