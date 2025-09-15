from pydantic import BaseModel, HttpUrl, ConfigDict


class FileSchema(BaseModel):
    """
    Описание структуры файла
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    filename: str
    directory: str
    url: HttpUrl

class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла
    """
    model_config = ConfigDict(populate_by_name=True)
    filename: str
    directory: str
    upload_file: str

class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла
    """
    file: FileSchema


