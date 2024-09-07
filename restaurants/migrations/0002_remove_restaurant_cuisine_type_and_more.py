# Generated by Django 5.1.1 on 2024-09-07 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='cuisine_type',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='description',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='google_place_id',
        ),
        migrations.RemoveField(
            model_name='review',
            name='created_at',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='place_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.TextField(),
        ),
    ]
