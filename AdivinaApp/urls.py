from django.urls import path
from . import views

urlpatterns = [
    path('', views.Adivina, name='AdivinaNumero'),
    path('resultado/', views.resultado, name='resultado'),
]