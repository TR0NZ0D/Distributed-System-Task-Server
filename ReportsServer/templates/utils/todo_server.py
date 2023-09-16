from . import constants
from .server_responses import TaskServerResponse, AllTasksServerResponse, Task
import requests


class __TodoServer:
    server_url = constants.todo_server_url

    def get_task(self, id: int) -> TaskServerResponse | None:
        try:
            request_url = self.server_url + f'/{id}'
            request = requests.get(request_url)
            response = self.__get_response_or_none(request)

            if response is None:
                return None

            return self.generate_task_response(response)
        except Exception as e:
            print(f'⛔ Failed to get task: {e}')
            return None

    def get_all_tasks(self) -> AllTasksServerResponse | None:
        try:
            request_url = self.server_url
            request = requests.get(request_url)
            response = self.__get_response_or_none(request)

            if response is None:
                return None

            return self.generate_all_tasks_response(response)
        except Exception as e:
            print(f'⛔ Failed to get all tasks: {e}')

    @staticmethod
    def __get_response_or_none(response: requests.Response) -> requests.Response | None:
        try:
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as errh:
            print(f'⛔ HTTP Error: {errh}')
        except requests.exceptions.ConnectionError as errc:
            print(f'⛔ Connection Error: {errc}')
        except requests.exceptions.Timeout as errt:
            print(f'⛔ Timeout Error: {errt}')
        except requests.exceptions.RequestException as err:
            print(f'⛔ Request Exception: {err}')
        except Exception as e:
            print(f'⛔ Generic Exception: {e}')

        return None

    @staticmethod
    def generate_task_response(response: requests.Response) -> TaskServerResponse | None:
        content = TaskServerResponse.generate_content(response)
        return TaskServerResponse(status=response.status_code, content=content)

    @staticmethod
    def generate_all_tasks_response(response: requests.Response) -> AllTasksServerResponse | None:
        content = AllTasksServerResponse.generate_content(response)
        return AllTasksServerResponse(status=response.status_code, content=content)


class __MockedTodoServer:
    server_url = 'http://localhost:8000/api/todo'
    mocked_task_1 = Task(id=1,
                         title="Mock task 01",
                         description="Mock my task 01",
                         created_at="2023-09-15T21:37:06.2463725",
                         completed_at=None,
                         is_completed=False)
    mocked_task_2 = Task(id=2,
                         title="Mock task 02",
                         description="Mock my task 02",
                         created_at="2023-09-15T21:37:10.1794322",
                         completed_at="2023-09-15T21:37:06.2463725",
                         is_completed=True)
    mocked_task_3 = Task(id=3,
                         title="Mock task 03",
                         description="Mock my task 03",
                         created_at="2023-09-15T21:37:06.2463725",
                         completed_at=None,
                         is_completed=False)
    mocked_task_4 = Task(id=4,
                         title="Mock task 04",
                         description="Mock my task 04",
                         created_at="2023-09-15T21:37:10.1794322",
                         completed_at="2023-09-15T21:37:06.2463725",
                         is_completed=True)

    def get_task(self, id: int) -> TaskServerResponse:
        match id:
            case 1:
                return TaskServerResponse(status=200,
                                          content=self.mocked_task_1)
            case 2:
                return TaskServerResponse(status=200,
                                          content=self.mocked_task_2)
            case 3:
                return TaskServerResponse(status=200,
                                          content=self.mocked_task_3)
            case 4:
                return TaskServerResponse(status=200,
                                          content=self.mocked_task_4)
            case _:
                return TaskServerResponse(status=404,
                                          content=None)

    def get_all_tasks(self) -> AllTasksServerResponse | None:
        return AllTasksServerResponse(status=200,
                                      content=[self.mocked_task_1, self.mocked_task_2,
                                               self.mocked_task_3, self.mocked_task_4])


todo_server = __TodoServer()
mocked_todo_server = __MockedTodoServer()
