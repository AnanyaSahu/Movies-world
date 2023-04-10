import requests
from geopy.geocoders import Nomination

# Method to obtain the user's current location
def get_location():
    geolocator = Nomination(user_agent="geoapiExercises")
    location = geolocator.geocode(input("Enter your current location: "))
    return location.latitude, location.longitude

# Method to search for nearby theatres
def search_theaters(api_key, latitude, longitude):
    api_key = "your_api_key"
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location.latitude},{location.longitude}&radius=5000&type=movie_theater&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data["results"]

# Method to Obtain details of nearby theatres and sort them based on their distance from the user's location
def get_nearby theaters(theaters, latitude, longitude):
    nearby theatres = []
    for theatre in theatres:
        name = theatre["name"]
        address = theatre["vicinity"]
        distance = theatre["geometry"]["location"]["lat"] - latitude + theatre["geometry"]["location"]["lng"] - longitude
        nearby_theatres.append({"name": name, "address": address, "distance": distance})
    nearby_theatres = sorted(nearby_theatres, key=lambda x: x["distance"])
    return nearby_theatres

# Method to Display the sorted list of nearby theatres to the user
def display_nearby_theatres(nearby_theatres):
    print("Nearby Theatres:")
    for theatre in nearby_theatres:
    print(f"{theatre['name']} ({theatre['address']}) - {theatre['distance']:.2f} km")

# Main method to get nearby theatres based on current location in sorted order
def main():
    api_key = "your_api_key"
    latitude, longitude = get_location()
    theatres = search_theatres(api_key, latitude, longitude)
    nearby_theatres = get_nearby_theatres(theatres, latitude, longitude)
    display_nearby_theatres(nearby_theatres)

if __name__ == "__main__":
    main()
