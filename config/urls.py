"""
URL configuration for config project.

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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="CurB backend API",
        default_version="v1",
        description="https://github.com/izunaaaaa/CurB_Backend",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("users.urls")),
    path("api/v1/feeds/", include("feeds.urls")),
    path("api/v1/groups/", include("groups.urls")),
    path("api/v1/letters/", include("letters.urls")),
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/comments/", include("comments.urls")),
    path("api/v1/recomments/", include("recomments.urls")),
    path("api/v1/likes/", include("likes.urls")),
    path("api/v1/letterlists/", include("letterlists.urls")),
    path("api/v1/access/", include("accessinfo.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
