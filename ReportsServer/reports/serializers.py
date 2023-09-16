from rest_framework import serializers

from . import models


class CompletedTaskReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompletedTaskReport
        fields = ['task_pk', 'task_created_at', 'task_completed_at']


class PendingTaskReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PendingTaskReport
        fields = ['task_pk', 'task_created_at']


class TasksCounterReportSerializer(serializers.ModelSerializer):
    completed_tasks_items = serializers.SerializerMethodField()
    pending_tasks_items = serializers.SerializerMethodField()

    def get_completed_tasks_items(self, obj: models.TasksCounterReport):
        if obj.completed_tasks.all():
            objs = []
            for c_obj in obj.completed_tasks.all():
                objs.append(c_obj.__getattribute__("serialize"))

            return objs
        return []

    def get_pending_tasks_items(self, obj: models.TasksCounterReport):
        if obj.pending_tasks.all():
            objs = []
            for c_obj in obj.pending_tasks.all():
                objs.append(c_obj.__getattribute__("serialize"))

            return objs
        return []

    class Meta:
        model = models.TasksCounterReport
        fields = ['task_count',
                  'completed_count',
                  'pending_count',
                  'completed_tasks_items',
                  'pending_tasks_items']
