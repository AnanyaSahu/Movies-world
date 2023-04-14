# import requests
from database import openDbConnection
# from geopy.geocoders import Nomination

# Method to obtain the user's current location
def get_location():
    # geolocator = Nomination(user_agent="geoapiExercises")
    # location = geolocator.geocode(input("Enter your current location: "))
    # return location.latitude, location.longitude
    pass

# Method to search for nearby theatres
def search_theaters(api_key, latitude, longitude):
    # api_key = "your_api_key"
    # url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location.latitude},{location.longitude}&radius=5000&type=movie_theater&key={api_key}"
    # response = requests.get(url)
    # data = response.json()
    # return data["results"]
    pass

def  getAreas():
    cursor = openDbConnection()
    getAreaQuery = "SELECT *FROM  [movieDb].[dbo].[Area];" 
    record = cursor.execute(getAreaQuery).fetchall()
    print(record)
    r= [tuple(row) for row in record]
    print(r)
    return {'rows': r}


# Method to Obtain details of nearby theatres and sort them based on their distance from the user's location
def get_nearby_theaters(area):
    cursor = openDbConnection()
    getNearByTheaterQuery = "SELECT t.thearerName, t.theaterId, a.areaId, a.areaName, abs(a.location-"+str(area)+"), t.rowRange, t.ColumnRange FROM [movieDb].[dbo].[Theater] t Inner join [movieDb].[dbo].Area a ON t.areaId = a.areaId group by t.thearerName, t.theaterId, a.areaId, a.areaName,abs(a.location-"+str(area)+"), t.rowRange, t.ColumnRange  order by abs(a.location-"+str(area)+");" 
    print(getNearByTheaterQuery)
    record = cursor.execute(getNearByTheaterQuery).fetchall()
    r= [tuple(row) for row in record]
    print(r)
    return {'rows': r}

    # nearby_theatres = []
    # for theatre in theatres:
    #     name = theatre["name"]
    #     address = theatre["vicinity"]
    #     distance = theatre["geometry"]["location"]["lat"] - latitude + theatre["geometry"]["location"]["lng"] - longitude
    #     nearby_theatres.append({"name": name, "address": address, "distance": distance})
    # nearby_theatres = sorted(nearby_theatres, key=lambda x: x["distance"])
    # return nearby_theatres

# def get_nearby_theaters(theaters, latitude, longitude):
#     nearby_theatres = []
#     for theatre in theatres:
#         name = theatre["name"]
#         address = theatre["vicinity"]
#         distance = theatre["geometry"]["location"]["lat"] - latitude + theatre["geometry"]["location"]["lng"] - longitude
#         nearby_theatres.append({"name": name, "address": address, "distance": distance})
#     nearby_theatres = sorted(nearby_theatres, key=lambda x: x["distance"])
#     return nearby_theatres

# Method to Display the sorted list of nearby theatres to the user
def display_nearby_theatres(nearby_theatres):
    # print("Nearby Theatres:")
    # for theatre in nearby_theatres:
    #  print(f"{theatre['name']} ({theatre['address']}) - {theatre['distance']:.2f} km")
    pass
# Main method to get nearby theatres based on current location in sorted order
# def main():
#     api_key = "your_api_key"
#     latitude, longitude = get_location()
#     theatres = search_theatres(api_key, latitude, longitude)
#     nearby_theatres = get_nearby_theatres(theatres, latitude, longitude)
#     display_nearby_theatres(nearby_theatres)

# if _name_ == "_main_":
#     main()


def getSeatsForMovie(theaterId,movieId):
    # sort closest to farthgest from ara
    return {'rows': []}
    

    
def getTheaters(area):
    # sort closest to farthgest from ara
    return {'rows': []}
    


# get_nearby_theaters(200)
