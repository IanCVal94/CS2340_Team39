from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from restaurants.models import Restaurant

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Restaurant, blank=True)  # Users can favorite restaurants

    def __str__(self):
        return self.user.username