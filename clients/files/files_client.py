from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict

class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла
    """
    filename: str
    directory: str
    upload_file: str

class FilesClient(ApiClient):
    """
    Клиент для работы с /api/v1/files
    """
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.
        :param file_id: Идентификатор файла
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/files/{file_id}")

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления объекта
        :param file_id: Идентификатор файла
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/files/{file_id}")

    def create_file_api(self, request) -> Response:
        """
        Метод создания объекта
        :param request: Словарь с filename, directory, upload_file
        :return:
        """
        return self.post(url="/api/v1/files", data=request, files={"Upload file": open(request['upload_file'], 'rb')})