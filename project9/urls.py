"""
URL configuration for project9 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',homepage,name='homepage'),
    path('indiateam/',indiateam,name='indiateam'),
    path('austeam/',austeam,name='austeam'),
    path('engteam/',engteam,name='engteam'),
    path('sriteam/',sriteam,name='sriteam'),
    path('witeam/',witeam,name='witeam'),
    path('matches/',matches,name='matches'),
    path('seriesm/',seriesm,name='seriesm'),
    path('live/',live,name='live'),
    path('live1/',live1,name='live1'),
    path('live2/',live2,name='live2'),
    path('live3/',live3,name='live3'),
    path('about/',about,name='about'),
]
