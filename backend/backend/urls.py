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
from django.conf import settings
from django.conf.urls import include
from rest_framework import routers
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, re_path

from users.api import views as user_views
from guides.api import views as guide_views
from runescape.api import views as runescape_views

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'guides', guide_views.GuideViewSet)
router.register(r'players', runescape_views.ClanMemberViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_auth.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

urlpatterns += [re_path(r'^.*(|/)/?$', TemplateView.as_view(template_name='index.html'))]
