function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.397, lng: 150.644},
        zoom: 8
    });

    // Add markers for restaurants
    restaurants.forEach(function(restaurant) {
        var marker = new google.maps.Marker({
            position: {lat: restaurant.lat, lng: restaurant.lng},
            map: map,
            title: restaurant.name
        });
    });
}

window.onload = initMap;