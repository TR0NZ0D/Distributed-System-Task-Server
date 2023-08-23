from django.db import models
from concurrency.fields import IntegerVersionField
from typing import Any


class CompletedTaskReport(models.Model):
    version = IntegerVersionField()
    task_pk = models.IntegerField("Task PK")
    created_at = models.DateTimeField("Created at", auto_now_add=True, editable=False)
    task_created_at = models.DateTimeField("Task created at", auto_now=False, auto_now_add=False)
    task_completed_at = models.DateTimeField("Task completed at", auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"Completed report for task {self.task_pk}"

    def __getattribute__(self, __name: str) -> Any:
        if __name == "serialize":
            return {
                "task_pk": self.task_pk,
                "task_created_at": self.task_created_at,
                "task_completed_at": self.task_completed_at
            }
        return super().__getattribute__(__name)

    class Meta:
        verbose_name = 'Completed task'
        verbose_name_plural = 'Completed tasks'


class PendingTaskReport(models.Model):
    version = IntegerVersionField()
    task_pk = models.IntegerField("Task PK")
    created_at = models.DateTimeField("Created at", auto_now_add=True, editable=False)
    task_created_at = models.DateTimeField("Task created at", auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"Pending report for task {self.task_pk}"

    def __getattribute__(self, __name: str) -> Any:
        if __name == "serialize":
            return {
                "task_pk": self.task_pk,
                "task_created_at": self.task_created_at
            }
        return super().__getattribute__(__name)

    class Meta:
        verbose_name = 'Pending task'
        verbose_name_plural = 'Pending tasks'


class TasksCounterReport(models.Model):
    version = IntegerVersionField()
    task_count = models.IntegerField("Created tasks")
    completed_count = models.IntegerField("Completed tasks")
    pending_count = models.IntegerField("Pending tasks")
    completed_tasks = models.ManyToManyField(CompletedTaskReport, verbose_name="Completed tasks", blank=True)
    pending_tasks = models.ManyToManyField(PendingTaskReport, verbose_name="Pending tasks", blank=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True, editable=False)

    def __str__(self):
        return "Tasks counter"

    class Meta:
        verbose_name = 'Task counter'
        verbose_name_plural = 'Task counters'
