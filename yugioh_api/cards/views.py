from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Card, Deck
from .serializers import CardSerializer, DeckSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

class CardListCreateView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CustomPagination(PageNumberPagination):
    page_size = 10  # Número de cartas por página
    page_size_query_param = 'page_size'
    max_page_size = 50

class BuscarCartaView(APIView):
    def get(self, request):
        name = request.query_params.get('name', None)
        card_type = request.query_params.get('card_type', None)
        rarity = request.query_params.get('rarity', None)
        level = request.query_params.get('level', None)

        # Filtrar las cartas según los parámetros recibidos
        cartas = Card.objects.all()

        if name:
            cartas = cartas.filter(name__icontains=name)
        if card_type:
            cartas = cartas.filter(card_type__icontains=card_type)
        if rarity:
            cartas = cartas.filter(rarity__icontains=rarity)
        if level:
            cartas = cartas.filter(level=level)  # Suponiendo que el nivel es un número entero

        # Ordenar las cartas y aplicar la paginación
        cartas = cartas.order_by('id')
        paginator = CustomPagination()
        paginated_cartas = paginator.paginate_queryset(cartas, request)
        serializer = CardSerializer(paginated_cartas, many=True)
        return paginator.get_paginated_response(serializer.data)


class DeckDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    
    def get_queryset(self):
        # Solo permite acceder al deck del usuario actual
        return self.queryset()


class DeckCreateView(generics.CreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    
    def get_queryset(self):
        # Solo devuelve los decks del usuario autenticado
        return self.queryset()
    
    def perform_create(self, serializer):
        # Asigna el usuario actual al deck
        serializer.save()

class DeckListCreateView(generics.ListCreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    def get_queryset(self):
        # Filtra los decks sin asociarlos a un usuario, ya que no hay un usuario vinculado
        return self.queryset  # Eliminar los paréntesis

    def perform_create(self, serializer):
        # Solo guarda el deck sin asociarlo a un usuario
        serializer.save()
