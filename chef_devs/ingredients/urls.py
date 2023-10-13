from django.urls import path
from . import views

app_name = 'ingredients'  

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout_info/', views.checkout_info, name='checkout_info'), 
    #path('/cart', views.cart, name='cart'),
]
