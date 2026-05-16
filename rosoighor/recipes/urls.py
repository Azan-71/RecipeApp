from django.urls import path
from . import views

urlpatterns = [
    path("", views.recipe_list, name="recipe_list"),   # matches /recipes/
    path("<int:pk>/", views.recipe_detail, name="recipe_detail"),
    path("add_recipe/", views.add_recipe, name="add_recipe"),
]
