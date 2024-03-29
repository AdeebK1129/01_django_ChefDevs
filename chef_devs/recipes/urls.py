from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe_info/', views.recipe_info, name='recipe_info'), 
    path('forms/', views.forms, name='forms'), 
    path('list_view/', views.list_view, name='list_view'), 
]
