from rest_framework import serializers
from .models import Card, Deck, DeckCard

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'  # Incluye todos los campos


class DeckCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeckCard
        fields = ('card', 'quantity')

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'  # O especifica los campos existentes si no quieres incluir todos

