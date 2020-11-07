"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from guides.api import views as guide_views
from rest_framework import permissions, routers
from runescape.api import views as runescape_views
from users.api import views as user_views
# from discord.api import views as discord_views

# Register API Routes
router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'guides', guide_views.GuideViewSet)
router.register(r'players', runescape_views.ClanMemberViewSet)

# API Docs Schema
schema_view = get_schema_view(
    openapi.Info(
        title='RsAtlantis API',
        default_version='v1',
        license=openapi.License(name='AGPL-3.0 License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

# API Doc Routes https://drf-yasg.readthedocs.io/en/stable/readme.html#usage
urlpatterns = [
    path('api/docs/swagger<str:format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

# Admin and API routes
urlpatterns += [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_auth.urls')),
    path('atlantisbot/', include('atlantisbot_api.urls')),
    path('api/', include(router.urls))
]
