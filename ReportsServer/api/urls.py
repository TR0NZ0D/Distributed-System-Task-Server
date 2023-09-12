from django.urls import path, include

from . import views

app_name = 'api'

urlpatterns = [
    # ======= API ======= #
    # path('', views..as_view(), name=""),

    # ======= Reports ======= #
    path('reports/', include('reports.urls')),
]
