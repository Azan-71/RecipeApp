from django.urls import path
from . import views

urlpatterns = [
    path('', views.comment_list, name='comment_list'),   # new hub route
    path('add/<int:recipe_id>/', views.add_comment, name='add_comment'),
    path('rate/<int:recipe_id>/', views.add_rating, name='add_rating'),
]