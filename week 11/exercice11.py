"""
This week, we're going to use the output we got to query the weather for a particular longitude-latitude pair of coordinates.
In this way, we will be able to retrieve the weather for any location in the Nominatim database.

This week's challenge is thus to write a function, "get_location_weather", which takes one argument, an address.
The address should be the same sort of thing that you passed to "find_city" last week, because the first thing that your function will have to do is call "find_city" to get the longitude and latitude of the address.

But then you're going to use the returned longitude and latitude in a query to OpenWeatherMap.org, using their API to retrieve information about the current weather at that point.

First: You'll need to sign up for an account here:
  https://openweathermap.org/

Once you register, you'll need to generate an API key.
This key consists of 32 hexadecimal digits, and is what you need to pass in your API requests in order to get a weather forecast.
You shouldn't share your API key with anyone; you'll notice that when I share my solution code, I'll keep that part blank.

The OWM API is in the form of a URL, whose arguments (name-value pairs) are passed in the URL itself, as part of a "GET" request.
You'll need to use the "requests" library to send the request, passing not just the latitude and longitude, but also the API ID that you generated, as the "appid" parameter.

I would also suggest sending the "units=metric" key-value pair, to avoid getting (for example) temperature in Kelvin.

Your function should return a Python dictionary with the following three key-value pairs:
temp, with the temperature
wind, with the wind speed
description, with a textual description of the current weather

So, when I run the following:
    mygeopy.get_location_weather('Modiin, Israel')
I get the following dict back:
    {'temp': 29.14, 'wind': 3.6, 'desc': 'clear sky'}
And when I invoke:
    mygeopy.get_location_weather('San Francisco, California')
I then get:
    {'temp': 17.56, 'wind': 3.1, 'desc': 'scattered clouds'}
If the "get_location_weather" function is given an address that doesn't have any location, then it should raise an AddressNotFound exception.
You'll need to define this exception and raise it under such circumstances.

The response will come back in JSON, so you'll have to interpret that and extract the right data from it.

Also note that I encountered some errors from Nominatim when I made too many requests in too short a time period, so if you get such errors, then give it some time.

"""
import requests
from week10 import exercice10
from geopy.geocoders import Nominatim

# api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={your api key}
# {'temp': 29.14, 'wind': 3.6, 'desc': 'clear sky'}


def find_city(address):
    geolocator = Nominatim(user_agent="Weekly Python Exercise")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None


class AddressNotFound(Exception):
    pass


def get_location_weather(location):
    if location is None:
        raise AddressNotFound(f'Cannot find location of "{location}"')
    latitude, longitude = find_city(location)
    datas = {'lat': latitude, 'lon': longitude, 'appid': '01cc51bb5280597ff9a8ddbd0311ef59'}
    response = requests.get(url='http://api.openweathermap.org/data/2.5/weather', params=datas)
    data = response.json()
    dict = {'temp': data['main']['temp'],
            'wind': data['wind']['speed'],
            'desc': data['weather'][0]['description']}
    print(dict)


get_location_weather('San Francisco, California')
