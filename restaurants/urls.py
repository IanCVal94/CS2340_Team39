from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_view, name='search'),
    path('detail/<int:restaurant_id>/', views.restaurant_detail_view, name='detail'),
    path('favorite/<int:restaurant_id>/', views.favorite_restaurant, name='favorite'),
]