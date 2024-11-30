import requests # type: ignore
from django.core.management.base import BaseCommand
from cards.models import Card

class Command(BaseCommand):
    help = 'Import Yu-Gi-Oh! cards from the external API'

    def handle(self, *args, **kwargs):
        url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
        response = requests.get(url)
        if response.status_code == 200:
            cards = response.json().get('data', [])
            for card in cards:
                Card.objects.update_or_create(
                    name=card.get('name'),
                    defaults={
                        'card_type': card.get('type'),
                        'description': card.get('desc'),
                        'level': card.get('level'),
                        'rarity': card.get('card_sets', [{}])[0].get('set_rarity'),
                        'image_url': card.get('card_images', [{}])[0].get('image_url'),
                    }
                )
            self.stdout.write(self.style.SUCCESS(f'Imported {len(cards)} cards'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch data from API'))
