# File: weather_parser.py
# Author: Jason Lu (jasonlu6@bu.edu)
# Collaborators: (CS 411 A1 Group 9)
# Allison Kaufman (alkauf@bu.edu)
# Carole Sung (carole07@bu.edu)
# Gabriela Carillo (gcarr@bu.edu)
# Date: 3/19/2017
# Description: This is a program that is modified to connect to an external API (such as
# Google Maps Weather or other website API) and get the data via XML, and use the
# Google Handler Class to parse the data from the User XML

# Reference / Source (modification):
# http://www.netinstructions.com/how-to-connect-to-an-api-and-parse-xml-and-why-you/

# import libraries
# importing the ur library request function
import urllib.request
# importing the XML SAX parser
import xml.sax

# series class that abstracts away the attributes of the data
class series:
    # Type: floating point
    # Store the Temperature of the User's Required location
    # Assume Fahrenheit for simplicity / prototyping
    # temperature_fahrenheit = []

    # Store the Temperature Low (daily) of the User's Required location
    lows = []

    # Store the Temperature High (daily) of the User's Required location
    highs = []

    # Later: store the humidity of the User's Required location
    # humidity = []

    # Day of the Week:
    # {Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday}
    days = []

    # forecast
    # forecast = {}

    # Optional: string dictionary to store the climates of the location(s)
    # climate = {}

# Google Handler class that extends to the default handler (to get the data from the user)
class GoogleHandler(xml.sax.ContentHandler):

    # method to get the elements (CREATE method)
    # try and catch exceptions other than the attributes required
    def getElement(self,name_query,attributes):
        # getting the day of the week
        if name_query == "day_of_the_week":
            # store in the attributes list
            print("Day:", attributes['data'])
            # append to the days list
            series.days.append(attributes['data'])
        # getting the low temperature of the data:
        elif name_query == "low":
            # store in the attributes list
            print("Low:", attributes['data'])
            # append to the low temperatures list
            series.lows.append(attributes['data'])
        # getting the high temperature of the data:
        elif name_query == "high":
            # store in the attributes list
            print("High:", attrs['data'])
            # append to the high temperatures list
            series.highs.append(attributes['data'])

    # make the HTTP request at specified URL
    url = input("Please enter a URL: ")
    # getting back the bunch of XML
    xmlRes = urllib.request.urlopen(str(url))
    # catching exceptions
    while True:
        try:
            url = 'http://www.google.com/iq/api?weather=Seattle+WA'
            break
        except ValueError:
            print("HTTP Error 404: URL not found")
            raise

    # print out the data:
    print("Printing out the data from the XML:")
    print(xmlRes)

    # creating the SAX parser
    par_xml = xml.sax.make_parser()
    # telling the parser to use the handler
    par_xml.setContentHandler(GoogleHandler())
    # parse the xml
    parsed = par_xml.parse(xmlRes)

    # Print out the lists (in attribute form:)
    print("Days:" , series.days)
    print("Lows:" , series.lows)
    print("Highs:", series.highs)







