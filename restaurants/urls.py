from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_restaurants, name='search'),
    path('restaurants/detail/<str:place_id>/', views.restaurant_detail_view, name='detail'),
    path('favorite/', views.favorite_restaurant, name='favorite'),
]