import requests
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    description: str | None
    created_at: str
    completed_at: str | None
    is_completed: bool

    def created_at_as_datetime(self) -> datetime:
        try:
            if self.created_at is None:
                return datetime.now()

            return datetime.fromisoformat(self.created_at)
        except Exception as e:
            print(f'Error converting created at to datetime object: {e}')
            return datetime.now()

    def completed_at_as_datetime(self) -> datetime:
        try:
            if self.completed_at is None:
                return datetime.now()

            return datetime.fromisoformat(self.completed_at)
        except Exception as e:
            print(f'Error converting completed at to datetime object: {e}')
            return datetime.now()


class __TaskServerResponseBase:
    @staticmethod
    def generate_content(response: requests.Response):
        return None


@dataclass
class TaskServerResponse(__TaskServerResponseBase):
    status: int
    content: Task | None

    @staticmethod
    def generate_content(response: requests.Response) -> Task | None:
        try:
            json = response.json()

            if isinstance(json, dict):
                return Task(json.get('id', 0),
                            json.get('title', ''),
                            json.get('description', None),
                            json.get('createdAt', ''),
                            json.get('completedAt', None),
                            json.get('isCompleted', False))

            print(f"Json is not a dict: {json}")
        except requests.exceptions.JSONDecodeError as jerr:
            print(f'Failed to decode json: {jerr}')

        return None


@dataclass
class AllTasksServerResponse(__TaskServerResponseBase):
    status: int
    content: list[Task]

    @staticmethod
    def generate_content(response: requests.Response) -> list[Task]:
        try:
            json = response.json()

            if isinstance(json, list):
                tasks = []

                for t_json in json:
                    task = Task(t_json.get('id', 0),
                                t_json.get('title', ''),
                                t_json.get('description', None),
                                t_json.get('createdAt', ''),
                                t_json.get('completedAt', None),
                                t_json.get('isCompleted', False))
                    tasks.append(task)

                return tasks

            print(f"Json is not a list: {json}")
        except requests.exceptions.JSONDecodeError as jerr:
            print(f'Failed to decode json: {jerr}')

        return []
