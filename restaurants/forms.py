from django.apps import AppConfig
from .models import Review
from django import forms

class RestaurantSearchForm(forms.Form):
    name = forms.CharField(required=False, label="Restaurant Name")
    location = forms.CharField(required=False, label="Location")
    cuisine = forms.CharField(required=False, label="Cuisine Type")
    distance = forms.IntegerField(required=False, label="Distance (in km)")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']

class accountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'