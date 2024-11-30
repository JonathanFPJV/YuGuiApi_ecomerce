# Generated by Django 5.1.3 on 2024-11-29 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('card_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('level', models.IntegerField(blank=True, null=True)),
                ('rarity', models.CharField(blank=True, max_length=50, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
