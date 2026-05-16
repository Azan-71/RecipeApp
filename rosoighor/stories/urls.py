from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('add/', views.add_story, name='add_story'),
    path('add/<int:recipe_id>/', views.add_story_for_recipe, name='add_story_for_recipe'),
]
