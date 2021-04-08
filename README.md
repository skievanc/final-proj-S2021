## Final Project: Script 1
### Web-scraping Weather Forecast Information with Python
This script scrapes a NWS weather forecast from weather.gov based on coordinates given by the user. 
The script asks the user to input a location as lat and lon values then fetches the forecast for that location from weather.gov.
The contents of the forecast is then formatted and put in a list, then printed out to the user.
Inputs taken are lattitude and longitude, as numbers, which are converted to strings to be used in the url for weather.gov.
Output given is the formated weather forecast for the input location.
  
The script functions as intended and I did not have issues adapting it.
Scraping information off the web with python is a useful tool I can see many uses for. In this code, it allows the user to easily look through many 
weather forecasts without having to type in and go to those addresses. This could be automated further for utility in a larger program.
  
## Final Project: Script 2
### Create graphs of frost dates based on NOAA historical climate data
This script takes a NOAA historical climate data set in csv format as input. The set must have atleast date and minimum temperature (TMIN) in it.
The dates of the first and last frosts are calculated for every year with data in the set.
Any NOAA historical data set in csv format with dates and TMIN will work.
Graphs with trend lines are output to visualize the dates. Dates shown as day of year.
  
First frost is defined here as the first freezing (<=32F) temperature day after the summer.
Last frost is defined here as the last freezing (<=32F) temperature day before the summer.
  
In creating this script I used the full historical daily summaries data set from Buffumville Lake, MA US (1959 - 2021) available online from NOAA. 
This station and data download can be found at https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USC00190998/detail.
A copy of this station data that I used is also included in the repository, 'buffumville_temps.csv'.
  
The script requires one of these NOAA historical datasets to run. The script is set up to ask for the address of the data; it can also be put in before running. 
  
The script is meant to identify the first and last occurances of frosts during the begining and end of the cold season, as defined above.
These are found for each year with the necessary data, then combined into a data set with only the first or last frost dates.
The output of the script are graphs which allow for interpretation of the frost dates.
For example: at Buffumville Lake, the date of the first frost is trending later, and the date of the last frost is trending early. This means the trend of the cold season is it is becoming shorter.   
If you use this data, you will notive there is an quite the outlier in last frost dates in 1990. This exists in the original data set, so it may be an error in the data. 
  
#### Writing the script
The idea of the script is based on a code I wrote in R for the same purpose. My goal was to learn more about using pandas and python in general for manipulating and visualizing data. 
I used pandas online reference and user guides for understanding the basics of pandas and using dataframes at https://pandas.pydata.org/docs/reference/. Stack Overflow for troubleshooting the many errors and issues I encountered at https://stackoverflow.com/. And realpython ploting guide for learning to make basic plots at https://realpython.com/pandas-plot-python/. 
  
I found writing this script I bit more challenging than anticipated, especially since I already had an outline for it from R. 
My first plan was to scrape historical weather data from the web to run the process on, but I found that to be a bit tricky, and instead decided to focus on manipulating and visualizing the data from a downloaded source.
I had many small errors and struggles, but most could be figured out by changing a few lines of code and checking for solutions online. 
My main recurring issue was and learning curve was dealing with adding, removing and changing entries in a dataframe. Part of the code is creating a new dataframe from only the frost dates, I learned the best way to do this is with lists, rather than iteratively adding directly to a new dataframe. 
  
Overall I am happy with the final script.


