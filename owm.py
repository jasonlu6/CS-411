# File: owm.py
# Author: Jason Lu (jasonlu6@bu.edu)
# Collaborators: (CS 411 A1 Group 9)
# Allison Kaufman (alkauf@bu.edu)
# Carole Sung (carole07@bu.edu)
# Gabriela Carillo (gcarr@bu.edu)
# Date: 3/22/2017
# Description: This is a program that will use the Online Weather Map
# to get data from a location and then using the OWM Python package
# return related information (climate, weather, geography, forecasts)
# so that it can be 'dumped' into XML form

# Github Source Documentation:
# https://github.com/csparpa/pyowm/blob/master/pyowm/docs/usage-examples.md

# FIX: why is the OWM import not working? (rest of it is fine, compiles)

from pyowm import OWM

class own_python:
    # get the API key for pyOWM
    API_key = 'G097IueS-9xN712E'
    owm = pyowm.OWM()

    # make sure the langauage is in English
    own_en = OWM()

class weather:
    # function to get the currently observed weather
    def getcurrentWeather():

        place = input("Please enter a location to get weather info: ")
        observed = own_python.owm.weather_at_place(place)
        city_id = int(input("Please enter the city id: "))
        observed = own_python.owm.weather_at_id(city_id)
        # get the latitude
        lat = float(input("Please enter the latitutde: "))
        long = float(input("Please enter the longitude: "))
        observed = own_python.owm.weather_at_coords(lat,long)

    # function to retrieve city ID
    def regCurrentWeather():
        # get the registry
        registration = own_python.owm.city_id_registry()
        # get the ID for the city
        city = input("Please enter a city: ")
        registration.ids_for(city)
        # bonus: gives instances of the cities
        registration.locations_for(city)

    # defining a global weather object
w = weather.getcurrentWeather().observed.get_weather()

    # get the temperature (in Celsius)
temp_cel = w.get_temperature(unit='celsius')
print("Temperature of location in Celsius is: " , temp_cel)

    # get the temperature (in Fahrenheit)
temp_fahren = w.get_temperature('fahrenheit')
print("Temperature of location in Fahrenheit is: ", temp_fahren)

# main function to print everything
def main():
    # getting the general information about the inputs
    print("Getting the city name: ")
    print(weather.getcurrentWeather.place)
    print("Getting the city id: ")
    print(weather.getcurrentWeather().city_id)
    print("Getting the city latitude: ")
    print(weather.getcurrentWeather().lat)
    print("Getting the city longitude: ")
    print(weather.getcurrentWeather().long)

main()











