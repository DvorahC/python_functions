"""
This week, we'll kick off both creating and using modules.
We'll use external modules -- sometimes from the Python standard library, and sometimes from PyPI -- to take advantage of the functionality that they offer.
We'll also write our own modules, so that we can import and use the functions we create.

The goal for this week is to create a module containing a function that takes a city name, and returns that city's longitude and latitude.

In order to do this, you'll need to download and install the "geopy" module from PyPI.
This module provides an interface to a variety of different mapping systems out on the Internet, including Google Maps, Bing Maps, and Open Street Map.
I'm going to suggest that you use the latter,
and that you particularly use its "Nominatim" interface -- but if you want to do something else, that's fine, too.

I then want you to create a module, "mygeopy", that acts as a wrapper around GeoPy.
In that module, define a function, "find_city", which takes one (string) argument, a city name.
The function should return a tuple containing the latitude and longitude of that city.
If the address isn't found, then we'll return None.

Note that in order to use Nominatim, you'll need to create a new geolocator object, via the "geocoders" module in the "geopy" package.
 You'll definitely want to look at the documentation for GeoPy, at:
    https://pypi.org/project/geopy/

"""
from geopy.geocoders import Nominatim


def find_city(address):
    geolocator = Nominatim(user_agent="Weekly Python Exercise")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None


find_city("Paris")
