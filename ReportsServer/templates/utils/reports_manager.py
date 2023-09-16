from .todo_server import todo_server, mocked_todo_server
from .server_responses import AllTasksServerResponse, Task, TaskServerResponse
from reports import models


class __ReportsManager:
    def save_task(self, response_or_task: TaskServerResponse | Task) -> models.CompletedTaskReport | models.PendingTaskReport | None:
        task: Task | None

        if isinstance(response_or_task, TaskServerResponse):
            task = response_or_task.content
        elif isinstance(response_or_task, Task):
            task = response_or_task
        else:
            return None

        if task is None:
            return None

        if task.is_completed:
            c_model = models.CompletedTaskReport.objects.create(task_pk=task.id,
                                                                task_created_at=task.created_at_as_datetime(),
                                                                task_completed_at=task.completed_at_as_datetime())
            return c_model

        p_model = models.PendingTaskReport.objects.create(task_pk=task.id,
                                                          task_created_at=task.created_at_as_datetime())
        return p_model

    def save_tasks(self, response_or_tasks: AllTasksServerResponse | list[Task]) -> list[models.CompletedTaskReport | models.PendingTaskReport] | None:
        tasks: list[Task] | None

        if isinstance(response_or_tasks, AllTasksServerResponse):
            tasks = response_or_tasks.content
        elif isinstance(response_or_tasks, list):
            tasks = response_or_tasks
        else:
            return None

        if tasks is None:
            return None

        models_list: list[models.CompletedTaskReport | models.PendingTaskReport] = []

        for task in tasks:
            task_model = self.save_task(task)

            if task_model is None:
                continue

            models_list.append(task_model)

        return models_list

    def count_tasks(self) -> models.TasksCounterReport | None:
        try:
            self.reset_task_count()
            completed_tasks = models.CompletedTaskReport.objects.all()
            pending_tasks = models.CompletedTaskReport.objects.all()
            completed_count = completed_tasks.count()
            pending_count = pending_tasks.count()
            task_count = completed_count + pending_count

            c_model = models.TasksCounterReport.objects.create(task_count=task_count,
                                                               completed_count=completed_count,
                                                               pending_count=pending_count)
            c_model.save()
            for c_task in completed_tasks:
                c_model.completed_tasks.add(c_task.pk)

            for p_task in pending_tasks:
                c_model.pending_tasks.add(p_task.pk)

            c_model.save()

            return c_model
        except Exception as e:
            print(f'Failed to count tasks: {e}')
            return None

    def reset_task_count(self) -> bool:
        if models.TasksCounterReport.objects.all().first() is not None:
            models.TasksCounterReport.objects.all().delete()
            if models.TasksCounterReport.objects.all().first() is not None:
                for t_counter in models.TasksCounterReport.objects.all():
                    t_counter.delete()

        counter_cleared = models.TasksCounterReport.objects.all().first() is None
        return counter_cleared

    def reset_database(self) -> bool:
        if models.CompletedTaskReport.objects.all().first() is not None:
            models.CompletedTaskReport.objects.all().delete()
            if models.CompletedTaskReport.objects.all().first() is not None:
                for c_task in models.CompletedTaskReport.objects.all():
                    c_task.delete()

        if models.PendingTaskReport.objects.all().first() is not None:
            models.PendingTaskReport.objects.all().delete()
            if models.PendingTaskReport.objects.all().first() is not None:
                for p_task in models.PendingTaskReport.objects.all():
                    p_task.delete()

        completed_cleared = models.CompletedTaskReport.objects.all().first() is None
        pending_cleared = models.PendingTaskReport.objects.all().first() is None
        counter_cleared = self.reset_task_count()

        return completed_cleared and pending_cleared and counter_cleared

    def refresh_database(self, response: TaskServerResponse | AllTasksServerResponse) -> bool:
        database_reset = self.reset_database()

        if not database_reset:
            print('Failed to reset database')

        tasks_created: bool = False

        if isinstance(response, TaskServerResponse):
            task = self.save_task(response)
            tasks_created = task is not None
        elif isinstance(response, AllTasksServerResponse):
            tasks = self.save_tasks(response)
            tasks_created = tasks is not None
        else:
            return False

        if not tasks_created:
            print('Failed to create tasks')

        count = self.count_tasks()

        success_counting_tasks = count is not None

        if not success_counting_tasks:
            print('Failed to count tasks')

        return database_reset and tasks_created and success_counting_tasks

    def populate_database(self) -> bool:
        tasks = todo_server.get_all_tasks()
        if tasks is None:
            return False

        return self.refresh_database(tasks)

    def populate_database_with_mocked_data(self) -> bool:
        mocked_tasks = mocked_todo_server.get_all_tasks()
        if mocked_tasks is None:
            return False

        return self.refresh_database(mocked_tasks)

    def get_all_completed_tasks(self):
        return models.CompletedTaskReport.objects.all()

    def get_all_pending_tasks(self):
        return models.PendingTaskReport.objects.all()

    def get_count(self):
        return models.TasksCounterReport.objects.last()


reports_manager = __ReportsManager()
