
from django.contrib import admin
from django.urls import path

app_name = 'surveys'

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()

