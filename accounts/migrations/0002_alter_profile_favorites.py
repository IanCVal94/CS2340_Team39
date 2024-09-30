# Generated by Django 5.1.1 on 2024-09-23 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('restaurants', '0003_remove_review_restaurant_review_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorites', to='restaurants.restaurant'),
        ),
    ]