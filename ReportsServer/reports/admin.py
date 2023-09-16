from django.contrib import admin
from . import models


class CompletedTaskReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'version', 'task_pk', 'task_created_at', 'task_completed_at', 'created_at')
    list_display_links = ('id', 'version')
    list_per_page = 35
    list_filter = ('task_created_at', 'task_completed_at', 'created_at')
    readonly_fields = ('id', 'version', 'task_pk', 'task_created_at', 'task_completed_at', 'created_at')


class PendingTaskReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'version', 'task_pk', 'task_created_at', 'created_at')
    list_display_links = ('id', 'version')
    list_per_page = 35
    list_filter = ('task_created_at', 'created_at')
    readonly_fields = ('id', 'version', 'task_pk', 'task_created_at', 'created_at')


class TasksCounterReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'version', 'task_count', 'completed_count', 'pending_count', 'created_at')
    list_display_links = ('id', 'version')
    list_per_page = 35
    list_filter = ('created_at',)
    readonly_fields = ('pk', 'version', 'task_count', 'completed_count', 'pending_count', 'completed_tasks', 'pending_tasks', 'created_at')


admin.site.register(models.CompletedTaskReport, CompletedTaskReportAdmin)
admin.site.register(models.PendingTaskReport, PendingTaskReportAdmin)
admin.site.register(models.TasksCounterReport, TasksCounterReportAdmin)
