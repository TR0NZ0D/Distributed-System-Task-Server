from django.urls import path, include

from . import views

app_name = 'api'

urlpatterns = [
    # ========== API Info ========== #
    path('info/status/', views.ApiStatus.as_view()),  # type: ignore
    path('info/version/', views.ApiVersion.as_view()),  # type: ignore

    # ======= Reports ======= #
    path('reports/', include('reports.urls')),
]
