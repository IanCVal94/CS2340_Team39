# Generated by Django 5.1.1 on 2024-09-26 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_remove_review_restaurant_review_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]