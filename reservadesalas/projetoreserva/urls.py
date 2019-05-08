from django.urls import path
from .views import InfoListView, InfoDetailView, InfoCreateView, InfoUpdateView, InfoDeleteView
from . import views

urlpatterns = [
    path('', InfoListView.as_view(), name='reserva-home'),
    path('info/<int:pk>/', InfoDetailView.as_view(), name='info-detail'),
    path('info/new/', InfoCreateView.as_view(), name='info-create'),
    path('info/<int:pk>/update/', InfoUpdateView.as_view(), name='info-update'),
    path('info/<int:pk>/delete/', InfoDeleteView.as_view(), name='info-delete'),
    path('sobre/', views.sobre, name='reserva-sobre'),

]