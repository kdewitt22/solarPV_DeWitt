from django.conf.urls import url, include
from django.urls import path

from . import views

app_name = 'register'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]