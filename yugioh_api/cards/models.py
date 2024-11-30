from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=255)
    card_type = models.CharField(max_length=100)  # Ejemplo: Monster, Spell, Trap
    description = models.TextField()
    level = models.IntegerField(null=True, blank=True)  # Solo aplica para cartas de monstruo
    rarity = models.CharField(max_length=50, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)  # URL de la imagen

    def __str__(self):
        return self.name
    

class Deck(models.Model):
    cards = models.ManyToManyField(
        'Card',
        through='DeckCard',
        through_fields=('deck', 'card'),
        related_name='decks'
    )

    def __str__(self):
        return f"Deck de {self.user.username}"

class DeckCard(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        # Reglas: máximo 3 copias de una carta
        if self.quantity > 3:
            raise ValueError("No se pueden agregar más de 3 copias de una misma carta.")
        super().save(*args, **kwargs)