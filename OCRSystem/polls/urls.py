from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="polls"),
    path('crew', views.crew, name='crew'),
]