import coreapi

from rest_framework import status
from rest_framework.response import Response
from rest_framework.schemas.coreapi import AutoSchema

from api.tools.api_tools import description_generator
from api.views import Base
from templates.utils.reports_manager import reports_manager
from templates.utils.constants import SHOULD_MOCK
from . import serializers
from . import models


# ============== Pending ============== #
class PendingTasksSchema(AutoSchema):
    def get_description(self, path: str, method: str) -> str:
        match method:
            case 'GET':
                responses = {
                    "200": {
                        'description': 'OK',
                        'reason': 'Pending tasks successfully requested'
                    },
                    "205": {
                        'description': 'RESET CONTENT',
                        'reason': 'Response was mocked'
                    },
                    "500": {
                        'description': 'INTERNAL SERVER ERROR',
                        'reason': 'Something went wrong while fetching'
                    }
                }
                return description_generator(title="Fetches all pending tasks in reports server",
                                             description='',
                                             responses=responses)
            case _:
                return ''

    def get_path_fields(self, path: str, method: str) -> list[coreapi.Field]:
        match method:
            case _:
                return []


class PendingTasks(Base):
    schema = PendingTasksSchema()

    def get(self, _):
        status_code: int

        if SHOULD_MOCK:
            success = reports_manager.populate_database_with_mocked_data()
            pending_tasks = reports_manager.get_all_pending_tasks()

            if pending_tasks is None or not success:
                return self.generate_basic_response(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                                    "Something went wrong while trying to get mocked pending tasks, please see server logs")

            tasks = pending_tasks
            status_code = status.HTTP_205_RESET_CONTENT

        else:
            success = reports_manager.populate_database()
            pending_tasks = reports_manager.get_all_pending_tasks()

            if pending_tasks is None or not success:
                return self.generate_basic_response(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                                    "Something went wrong while trying to get pending tasks, please see server logs")

            tasks = pending_tasks
            status_code = status.HTTP_200_OK

        mocked_warning = ' [Mocked]' if SHOULD_MOCK else ''

        response_data = self.generate_basic_response_data(status_code,
                                                          f"{tasks.count()} pending task(s) found{mocked_warning}")
        serializer = serializers.PendingTaskReportSerializer(tasks, many=True)
        response_data["content"] = serializer.data
        return Response(data=response_data, status=status_code)


# ============== Completed ============== #
class CompletedTasksSchema(AutoSchema):
    def get_description(self, path: str, method: str) -> str:
        match method:
            case 'GET':
                responses = {
                    "200": {
                        'description': 'OK',
                        'reason': 'Completed tasks successfully requested'
                    },
                    "205": {
                        'description': 'RESET CONTENT',
                        'reason': 'Response was mocked'
                    },
                    "500": {
                        'description': 'INTERNAL SERVER ERROR',
                        'reason': 'Something went wrong while fetching'
                    }
                }
                return description_generator(title="Fetches all completed tasks in report server",
                                             description='',
                                             responses=responses)
            case _:
                return ''

    def get_path_fields(self, path: str, method: str) -> list[coreapi.Field]:
        match method:
            case _:
                return []


class CompletedTasks(Base):
    schema = CompletedTasksSchema()

    def get(self, _):
        status_code: int

        if SHOULD_MOCK:
            success = reports_manager.populate_database_with_mocked_data()
            completed_tasks = reports_manager.get_all_completed_tasks()

            if completed_tasks is None or not success:
                return self.generate_basic_response(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                                    "Something went wrong while trying to get mocked completed tasks, please see server logs")

            tasks = completed_tasks
            status_code = status.HTTP_205_RESET_CONTENT

        else:
            success = reports_manager.populate_database()
            completed_tasks = reports_manager.get_all_completed_tasks()

            if completed_tasks is None or not success:
                return self.generate_basic_response(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                                    "Something went wrong while trying to get completed tasks, please see server logs")

            tasks = completed_tasks
            status_code = status.HTTP_200_OK

        mocked_warning = ' [Mocked]' if SHOULD_MOCK else ''

        response_data = self.generate_basic_response_data(status_code,
                                                          f"{tasks.count()} completed task(s) found{mocked_warning}")
        serializer = serializers.CompletedTaskReportSerializer(tasks, many=True)
        response_data["content"] = serializer.data
        return Response(data=response_data, status=status_code)


# ============== Count ============== #
class TaskCountSchema(AutoSchema):
    def get_description(self, path: str, method: str) -> str:
        match method:
            case 'GET':
                responses = {
                    "200": {
                        'description': 'OK',
                        'reason': 'Tasks count successfully requested'
                    },
                    "205": {
                        'description': 'RESET CONTENT',
                        'reason': 'Response was mocked'
                    },
                    "500": {
                        'description': 'INTERNAL SERVER ERROR',
                        'reason': 'Something went wrong while fetching'
                    }
                }
                return description_generator(title="Counts all tasks in reports server",
                                             description='',
                                             responses=responses)
            case _:
                return ''

    def get_path_fields(self, path: str, method: str) -> list[coreapi.Field]:
        match method:
            case _:
                return []


class TaskCount(Base):
    schema = TaskCountSchema()

    def get(self, _):
        count: models.TasksCounterReport
        status_code: int

        if SHOULD_MOCK:
            success = reports_manager.populate_database_with_mocked_data()
            t_count = reports_manager.get_count()

            if t_count is None or not success:
                return self.generate_basic_response(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                                    "Something went wrong while trying to count mocked tasks, please see server logs")

            count = t_count
            status_code = status.HTTP_205_RESET_CONTENT

        else:
            success = reports_manager.populate_database()
            t_count = reports_manager.get_count()

            if t_count is None or not success:
                return self.generate_basic_response(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                                    "Something went wrong while trying to count tasks, please see server logs")

            count = t_count
            status_code = status.HTTP_200_OK

        mocked_warning = ' [Mocked]' if SHOULD_MOCK else ''

        response_data = self.generate_basic_response_data(status_code,
                                                          f"Tasks successfully counted{mocked_warning}")
        serializer = serializers.TasksCounterReportSerializer(count, many=False)
        response_data["content"] = serializer.data
        return Response(data=response_data, status=status_code)
