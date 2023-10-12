from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe_info/', views.index, name='recipe_info'),  
]