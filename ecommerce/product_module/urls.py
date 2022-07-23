from os import remove
from django.urls import path
from .views import index, cart, removeCart, success_page, error_page

urlpatterns = [
    path('', index, name="index"),
    path('cart/', cart, name="cart"),
    path('cart/remove/<int:id>', removeCart),
    path('success_page/', success_page, name="success_page"),
    path('error_page/', error_page, name="error_page"),
]