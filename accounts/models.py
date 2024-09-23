from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from restaurants.models import Restaurant

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Restaurant, related_name="favorites", blank=True)

    def favorite(self, restaurant):
        self.favorites.add(restaurant)

    def unfavorite(self, restaurant):
        self.favorites.remove(restaurant)

    def has_favorited(self, restaurant):
        return self.favorites.filter(restaurant=restaurant).exists()

    def __str__(self):
        return self.user.username