'''
Author: Evan Collins
IDCE302
Created 4/6/2021

This script takes a NOAA historical climate data set in csv format as input. The set must have minimum temperature (TMIN) in it.
The dates of the first and last frosts are calculated for every year with data in the set.
Any NOAA historical data set in csv format with dates and TMIN will work.
Graphs with trend lines are output to visualize the dates. Dates shown as day of year.

First frost is defined here as the first freezing (<=32F) temperature day after the summer.
Last frost is defined here as the last freezing (<=32F) temperature day before the summer.

'''

## Setup
# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as plb

# Load in data
in_table = input('Enter full csv data set address:')
#in_table = 'ADDRESS HERE'

# Bring table into python as pandas dataframe
tdata = pd.read_csv(in_table)

# Turn date column in datetime type
# Extract month and year into a new columns
tdata['DATE']=pd.to_datetime(tdata['DATE'])
tdata['MONTH'] = tdata['DATE'].dt.month
tdata['YEAR'] = tdata['DATE'].dt.year


## Find the first and last frost dates of every year

# Assign a season to each day
# 1 is first half of year, 2 is second half of year
# 1 represents last frost dates, 2 represents first frost dates
tdata['SEASON']=''
i=0
for m in tdata['MONTH']:
    if m<8:                     # January - July assigned season 1
        tdata.at[i,'SEASON']=1
    else:                       # August - December assigned season 2
        tdata.at[i,'SEASON']=2
    i+=1

# Create a new smaller data frame with only freezing temperatures (<=32F)
t32=tdata[tdata['TMIN']<=32]


# Create two lists, one for each set of frost dates
# A last frost is the last 32F temp of the year before summer (season 1)
# A first frost is the first 32 F temp after the summer (season 2)
# The lists hold the dataframe rows of the last or first frost dates as lists
year = int(t32['YEAR'].head(1))  # Find the first year in the dataset
first_f= list()
last_f= list()
while year < int(t32['YEAR'].tail(1)):  # Find dates for every year from first year to year before last (this excludes incomplete year 2021)

    f_temp=t32[(t32['YEAR']==year) & (t32['SEASON']==1)]       # Subset year being checked and season 1
    if not f_temp.empty:                                       # Confirm year & season are not empty
      last_f.append(f_temp.tail(1).values.flatten().tolist())  # Add row of last frost date from dataframe to list

    f_temp=t32[(t32['YEAR'] == year) & (t32['SEASON'] == 2)]    # Subset year being checked and season 2
    if not f_temp.empty:                                        # Confirm year & season are not empty
      first_f.append(f_temp.head(1).values.flatten().tolist())  # Add row of first frost date from dataframe to list

    year+=1  # iterate through every year in dataframe

# Create new dataframes for each set of frost dates from the lists
firstfrost = pd.DataFrame(first_f, columns=['STATION','NAME','DATE','TMAX','TMIN','MONTH','YEAR','SEASON'])
lastfrost = pd.DataFrame(last_f, columns=['STATION','NAME','DATE','TMAX','TMIN','MONTH','YEAR','SEASON'])

# Create day of year column to display frost date
firstfrost['DAY_OF_YEAR']=firstfrost['DATE'].dt.dayofyear
lastfrost['DAY_OF_YEAR']=lastfrost['DATE'].dt.dayofyear


## Visualize frost dates
# Shows frost date on y-axis as day of year, year on x-axis
# Scatter plot of points, with trend line

# Plot of first frosts
firstfrost.plot(x='YEAR',y='DAY_OF_YEAR',kind='scatter')          # Create the scatter plot
z = np.polyfit(firstfrost['YEAR'], firstfrost['DAY_OF_YEAR'], 1)  # Create a trend line
p = np.poly1d(z)
plb.plot(firstfrost['YEAR'],p(firstfrost['YEAR']),'-r')           # Add trend line to plot
plt.show()                                                        # Display graph

# Plot of last frosts
lastfrost.plot(x='YEAR',y='DAY_OF_YEAR')                        # Create the scatter plot
z = np.polyfit(lastfrost['YEAR'], lastfrost['DAY_OF_YEAR'], 1)  # Create a trend line
p = np.poly1d(z)
plb.plot(lastfrost['YEAR'],p(lastfrost['YEAR']),'-r')           # Add trend line to plot
plt.show()                                                      # Display graph
