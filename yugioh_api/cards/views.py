from django.shortcuts import render

from rest_framework import generics
from .models import Card
from .serializers import CardSerializer
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
        if name:
            # Ordena las cartas por un campo específico
            cartas = Card.objects.filter(name__icontains=name).order_by('id')
            paginator = CustomPagination()
            paginated_cartas = paginator.paginate_queryset(cartas, request)
            serializer = CardSerializer(paginated_cartas, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response({"error": "Debe proporcionar un nombre para buscar"}, status=status.HTTP_400_BAD_REQUEST)
