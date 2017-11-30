import requests
from .models import Hotel
def get_hotel_id(hotel_id):
    API_KEY = "AIzaSyB_1H2SfrFsQ5gWMbV1q-V-uVuNV_OkbQQ"
    hotel = Hotel.objects.get(pk=hotel_id)
    address = hotel.address
    address = address.replace(" ","+").strip()
    SEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key=AIzaSyDLF1HytJluUKWh4iMzPSqosF1UCvdOB38".format(address)
    #print(SEARCH_URL)
    json_data = requests.get(SEARCH_URL).json()
    result_list = json_data["results"]

    for dictionary in result_list[:1]:
        place_id = dictionary["place_id"]



    # PIN_URL = "https://www.google.com/maps/embed/v1/place?key=AIzaSyB_1H2SfrFsQ5gWMbV1q-V-uVuNV_OkbQQ" \
    #           "&q=place_id{}".format(place_id)

    PIN_URL = "https://www.google.com/maps/embed/v1/place" \
              "?key={}" \
              "&q=place_id:{}".format(API_KEY,place_id)




    return PIN_URL
