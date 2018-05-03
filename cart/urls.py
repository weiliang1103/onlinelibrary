from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.view_cart, name='cart-view'),
    path('add/', views.add_to_cart, name='cart-add'),
    path('delete/', views.remove_from_cart, name='cart-remove'),
    path('delete/all', views.empty_cart, name='cart-empty'),
    path('checkout', views.checkout, name='cart-checkout'),
]
