"""
{
  "id": "string",
  "title": "string",
  "maxScore": 0,
  "minScore": 0,
  "description": "string",
  "estimatedTime": "string"
}
"""
from pydantic import BaseModel, Field
from dataclasses import dataclass, asdict
class CourseSchema(BaseModel):
    id: str = Field()
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str


course_default_model = CourseSchema(
    id="4124123",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    estimatedTime="1 week"
)

course_json = """{
    "id": "123123123",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}"""


course_dict_model = CourseSchema.model_validate_json(course_json)
print(course_dict_model)







