import googlemaps
from django.conf import settings
import math

class GooglePlacesService:
    def __init__(self):
        self.client = googlemaps.Client(key=settings.GOOGLE_API_KEY)

    def get_place_details(self, place_id):
        return self.client.place(place_id=place_id)

    def search_restaurants(self, query, location=None, cuisine=None, rating=None, radius=5000):
        search_query = query or ""
        if cuisine:
            search_query += f" {cuisine} restaurant"

        try:
            places_result = self.client.places(
                query=search_query,
                location=location,
                radius=radius,
                type='restaurant'
            )
        except Exception as e:
            print(f"Error during API request: {e}")
            return []

        restaurants = []

        for place in places_result.get('results', []):
            if rating and place.get('rating', 0) < int(rating):
                continue
            restaurants.append({
                'id': place.get('place_id', ''),
                'name': place['name'],
                'location': place.get('formatted_address', 'No Address'),
                'latitude': place['geometry']['location']['lat'],
                'longitude': place['geometry']['location']['lng'],
                'rating': place.get('rating', 'No Rating')
            })

        return restaurants