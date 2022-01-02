"""nepali_municipalities URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Municaplites Resource API",
        default_version='v1',
        description="Flight Resource API",
    ),
)
from apps.municaplities import views
import debug_toolbar

urlpatterns = [
    path(
        'api/docs/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='api-docs'
    ),
    path('admin/', admin.site.urls),
    path('municipalities/add', views.CreateMunicipalites.as_view()),
    path('municipalities/search', views.ListMunicipalitiesView.as_view()),
    path('municipalities/all-data', views.ListAllDataView.as_view()),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    SHOW_TOOLBAR_CALLBACK = True
