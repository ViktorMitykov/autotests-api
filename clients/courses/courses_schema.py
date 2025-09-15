from pydantic import BaseModel, Field, ConfigDict
from clients.users.users_schema import UserSchema
from clients.files.files_schema import FileSchema


class CourseSchema(BaseModel):
    """
    Описание структуры курса
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")

class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса получения курса
    """
    user_id: str = Field(alias="userId")

class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")

class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса
    """
    course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры обновления создание курса
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

