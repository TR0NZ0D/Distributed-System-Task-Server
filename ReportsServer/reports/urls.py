from django.urls import path

from . import views

app_name = 'reports'

urlpatterns = [
    # ======= Pending ======= #
    path('pending/', views.PendingTasks.as_view()),  # type: ignore

    # ======= Completed ======= #
    path('completed/', views.CompletedTasks.as_view()),  # type: ignore

    # ======= Count ======= #
    path('count/', views.TaskCount.as_view()),  # type: ignore
]
