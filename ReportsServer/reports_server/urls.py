"""
URL configuration for reports_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework_swagger.views import get_swagger_view

schema_url_patterns = [
    path('api/', include('api.urls'))
]

swagger_view = get_swagger_view(title="Reports Server - API",
                                patterns=schema_url_patterns)

urlpatterns = [
    # ========== Home screen ========== #
    path('', RedirectView.as_view(pattern_name='swagger_docs', permanent=True)),

    # ======== API ======== #
    path('api/', include('api.urls')),
    path('api/docs/', swagger_view, name="swagger_docs"),  # type: ignore

    # ======== Admin Interface ======== #
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # type: ignore
