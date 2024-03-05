from django.urls import path

from . import views

app_name = 'ssanmyApp'

urlpatterns = [
    path('', views.index),
]