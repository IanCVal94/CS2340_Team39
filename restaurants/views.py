import requests
from django.http import JsonResponse, Http404
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .google_places_service import GooglePlacesService
import math
from django.shortcuts import render
from .models import Restaurant
from math import radians, sin, cos, sqrt, atan2


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def search_view(request):
    # Example latitude and longitude for the user
    user_lat = float(request.GET.get('lat', 33.7488))  # Default to Atlanta if not provided
    user_lng = float(request.GET.get('lng', -84.3877))  # Default to Atlanta if not provided

    # Fetch restaurants from database (example query)
    restaurants = Restaurant.objects.all()

    # Calculate distances and sort
    for restaurant in restaurants:
        restaurant.distance = haversine(user_lat, user_lng, restaurant.latitude, restaurant.longitude)

    sorted_restaurants = sorted(restaurants, key=lambda r: r.distance)

    return render(request, 'restaurants/search.html', {'restaurants': sorted_restaurants})

def search_restaurants(request):
    query = request.GET.get('q')
    cuisine = request.GET.get('cuisine')
    user_location = request.GET.get('address')
    rating = request.GET.get('rating')
    max_distance = int(request.GET.get('distance', 10))  # Get the max distance from the form

    google_places = GooglePlacesService()

    if user_location:
        try:
            user_location_data = google_places.client.geocode(user_location)
            if user_location_data:
                user_lat = user_location_data[0]['geometry']['location']['lat']
                user_lng = user_location_data[0]['geometry']['location']['lng']
            else:
                user_lat, user_lng = 33.7488, -84.3877  # Default to some coordinates if geocoding fails
        except Exception as e:
            print(f"Error geocoding location: {e}")
            user_lat, user_lng = 33.7488, -84.3877
    else:
        user_lat, user_lng = 33.7488, -84.3877  # Default coordinates if no location is provided

    try:
        # Fetch restaurants with a larger radius initially
        all_restaurants = google_places.search_restaurants(query, user_location, cuisine, rating, radius=20000)
        filtered_restaurants = []

        for restaurant in all_restaurants:
            distance = haversine(user_lat, user_lng, restaurant['latitude'], restaurant['longitude'])
            if distance <= max_distance:
                restaurant['distance'] = distance  # Add distance to the restaurant data
                filtered_restaurants.append(restaurant)

        filtered_restaurants.sort(key=lambda r: r['distance'])  # Sort by distance

        return render(request, 'restaurants/search.html', {'restaurants': filtered_restaurants})
    except Exception as e:
        print(f"Error fetching restaurants: {e}")
        return render(request, 'restaurants/search.html', {'restaurants': []})


def restaurant_detail_view(request, place_id):
    # Construct the API request URL
    api_key = settings.GOOGLE_API_KEY  # Ensure this is set in your settings
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}"

    #print(url)

    # Make the request to the Google Places API
    response = requests.get(url)
    data = response.json()

    # Check if the response is successful and contains the needed data
    if response.status_code != 200 or 'result' not in data:
        raise Http404("Restaurant not found.")

    # Extract relevant data from the response
    restaurant_data = data['result']
    photo_reference = restaurant_data['photos'][0]['photo_reference']
    restaurant_image = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}"

    # Render your template using the restaurant data
    return render(request, 'restaurants/detail.html', {'restaurant_data': restaurant_data, 'GOOGLE_API_KEY': api_key, 'restaurant_image': restaurant_image})



@login_required
def favorite_restaurant(request):
    place_id = request.GET.get('place_id')  # Get place_id from query parameters

    # get name to pass in somehow

    if not place_id:
        return redirect('search')  # Redirect if no place_id provided

    restaurant, created = Restaurant.objects.get_or_create(place_id=place_id)
    profile = request.user.profile
    if restaurant in profile.favorites.all():
        profile.favorites.remove(restaurant)
    else:
        profile.favorites.add(restaurant)

    return redirect('detail', place_id=place_id)
