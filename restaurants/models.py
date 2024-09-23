from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Restaurant(models.Model):
    place_id = models.CharField(max_length=255, unique=True, null=True, blank=True)  # Ensure place_id exists
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)  # Allow null and blank values
    longitude = models.FloatField(null=True, blank=True)  # Allow null and blank values
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.CharField(max_length=255)
    review_text = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


