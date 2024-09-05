from django.shortcuts import get_object_or_404, render, redirect
from .models import Restaurant
from django.contrib.auth.decorators import login_required

def search_view(request):
    query = request.GET.get('q')
    cuisine = request.GET.get('cuisine')
    location = request.GET.get('location')

    restaurants = Restaurant.objects.all()

    if query:
        restaurants = restaurants.filter(name__icontains=query)
    if cuisine:
        restaurants = restaurants.filter(cuisine_type__icontains=cuisine)
    if location:
        restaurants = restaurants.filter(location__icontains=location)

    return render(request, 'restaurants/search.html', {'restaurants': restaurants})

def restaurant_detail_view(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    reviews = restaurant.reviews.all()  # Get all reviews for the restaurant
    return render(request, 'restaurants/detail.html', {'restaurant': restaurant, 'reviews': reviews})

@login_required
def favorite_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    profile = request.user.profile
    if restaurant in profile.favorites.all():
        profile.favorites.remove(restaurant)
    else:
        profile.favorites.add(restaurant)
    return redirect('detail', restaurant_id=restaurant_id)
