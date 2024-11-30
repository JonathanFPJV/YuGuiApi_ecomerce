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