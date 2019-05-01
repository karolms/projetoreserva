from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='reserva-home'),
    path('sobre/', views.sobre, name='reserva-sobre'),
]