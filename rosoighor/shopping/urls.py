from django.urls import path
from . import views

urlpatterns = [
    path('', views.tip_list, name='tip_list'),
]