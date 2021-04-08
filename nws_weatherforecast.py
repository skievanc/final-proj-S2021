# -*- coding: utf-8 -*-
"""NWS_WeatherForecast.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1md_kKqJdTDrnp3aBK_4qmmotBFklbhak
"""

'''
Author: Evan Collins
IDCE302
Created: 4/6/2021
'''
## The script asks the user to input a location as lat and lon values then fetches the forecast
## for that location from weather.gov.
## The contents of the forecast is then formatted and put in a list, then printed out to the user
## Inputs: Lat and long, as numbers, which are converted to strings
## Outputs: The weather forecast for input location

# import required libraries
import requests
from bs4 import BeautifulSoup

# Create an empty list to store response
forecast = []

# Ask the user for a lattitude and longitude to search the forescast
# Convert input for lat and lon to str for concatenation
lat = str(input("Enter a lattitude:")) 
lon = str(input("Enter a longitude:")) 

# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})

# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list
# Add space between words
for i in weather_forecast:
    i = i.text
    x=1
    while x < len(i)-1:                       # Loop through string
       if i[x].islower() & i[x+1].isupper():  # Create space between words by comparing case
         i = i[:x+1]+" "+i[x+1:]
       x+=1
    forecast.append(i.upper())                # Add to list in uppercase

# Print list to remove unicode characters
for day in forecast:
    print(day)