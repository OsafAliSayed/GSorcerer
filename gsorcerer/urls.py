from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('organization/<str:org_slug>' , views.organization, name='organization'),
]
