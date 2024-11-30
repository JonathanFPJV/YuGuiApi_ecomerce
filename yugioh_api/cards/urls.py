from django.urls import path
from .views import BuscarCartaView, CardListCreateView, CardDetailView

urlpatterns = [
    path('cards/', CardListCreateView.as_view(), name='card-list'),
    path('cards/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('cards/buscar/', BuscarCartaView.as_view(), name='buscar_carta'),
]
