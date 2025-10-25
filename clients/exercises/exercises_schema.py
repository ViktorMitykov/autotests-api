from typing import Annotated
from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake

class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнение
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class GetExerciseQuerySchema(BaseModel):
    """
    Описание структуры запроса для получения упражнение
    """
    model_config = ConfigDict(populate_by_name=True)
    courseId: str = Field(alias="courseId")

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры запроса для получения списка упражнение
    """
    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа для получения упражнение
    """
    exercise: ExerciseSchema

class CreateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса для создания упражнение
    """
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания упражнение
    """
    exercise: ExerciseSchema

class UpdateExerciseRequestApiSchema(BaseModel):
    """
    Описание структуры запроса для обновления упражнение
    """
    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class UpdateExerciseResponseApiSchema(BaseModel):
    """
    Описание структуры ответа для обновления упражнение
    """
    exercise: ExerciseSchema

