from rest_framework import serializers
from .models import Card, Deck, DeckCard

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'  # Incluye todos los campos


class DeckCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeckCard
        fields = ('card', 'quantity')  # Campos necesarios para la relación

class DeckSerializer(serializers.ModelSerializer):
    cards = DeckCardSerializer(many=True, write_only=True)  # Campo para agregar cartas al deck
    deck_cards = DeckCardSerializer(many=True, read_only=True, source='deckcard_set')  # Leer las cartas del deck

    class Meta:
        model = Deck
        fields = ('id', 'cards', 'deck_cards')  # Incluye tanto la entrada como la salida

    def create(self, validated_data):
        # Extraer cartas del deck del payload
        cards_data = validated_data.pop('cards', [])
        deck = Deck.objects.create(**validated_data)

        # Crear las relaciones con DeckCard
        for card_data in cards_data:
            DeckCard.objects.create(
                deck=deck,
                card=card_data['card'],
                quantity=card_data['quantity']
            )
        return deck

    def update(self, instance, validated_data):
        # Actualizar cartas en el deck
        cards_data = validated_data.pop('cards', [])
        instance = super().update(instance, validated_data)

        # Limpiar cartas actuales y agregar nuevas
        instance.deckcard_set.all().delete()
        for card_data in cards_data:
            DeckCard.objects.create(
                deck=instance,
                card=card_data['card'],
                quantity=card_data['quantity']
            )
        return instance
