from tabnanny import check
from django import conf
from django.urls import path
from .views import confirmpayment

urlpatterns = [
    path('checkout/', confirmpayment),
]