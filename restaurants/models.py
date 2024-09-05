from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    cuisine_type = models.CharField(max_length=100)
    location = models.CharField(max_length=255)  # Could be a text address or lat/long
    rating = models.DecimalField(max_digits=2, decimal_places=1)  # 0-10 rating scale
    google_place_id = models.CharField(max_length=100, blank=True, null=True)  # For Google Maps integration
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)  # Rating out of 5 stars
    review_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review of {self.restaurant.name}"

