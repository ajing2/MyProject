"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path


from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter



from rest_framework_swagger.views import get_swagger_view

from ansible import views

schema_view = get_swagger_view(title='API')


urlpatterns = [
    url(r'websocket', views.websocket),
    url(r'echo$', views.echo),
    url(r'scripts/$', views.scripts),
    url(r'webssh/$', views.webssh),
    url(r'ws/$', views.ws),

]