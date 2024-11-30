from django.urls import path
from .views import BuscarCartaView, CardListCreateView, CardDetailView, DeckCreateView, DeckDetailView, DeckListCreateView

urlpatterns = [
    path('cards/', CardListCreateView.as_view(), name='card-list'),
    path('cards/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('cards/buscar/', BuscarCartaView.as_view(), name='buscar_carta'),
    path('deck/', DeckCreateView.as_view(), name='deck-create'),
    path('deck/<int:pk>/', DeckDetailView.as_view(), name='deck-detail'),
    path('decks/', DeckListCreateView.as_view(), name='deck-list-create'),
]
