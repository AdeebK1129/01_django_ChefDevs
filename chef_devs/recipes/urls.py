from django.urls import path

from . import views

app_name = "recipes"

urlpatterns = [
   path("", views.index, name="index"),
   path("cookies", views.cookies, name="cookies"),
]
