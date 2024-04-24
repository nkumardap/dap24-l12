import pandas as pd
import matplotlib.pyplot as plt

"""
Today we will continue exploring weather data for a fictional city using 
weather_data.csv. It contains the following variables:

Date: The date for each recorded weather observation. Formatted as YYYY-MM-DD.
Max Temperature: The maximum temperature recorded on a given day, measured in 
    degrees Celsius
Min Temperature: The minimum temperature recorded on a given day, measured in 
    degrees Celsius
Precipitation: The amount of precipitation recorded on a given day, measured 
    in millimeters
Wind Speed: The average wind speed recorded on a given day, measured in 
    kilometers per hour
Humidity: The average humidity percentage recorded on a given day
"""

"""
EXERCISE 1

Short: Create a dual plot axes containing wind speed and humidity for this city

Long: Open the file weather_data.csv and convert Date to a datetime object. Remember
to use assignment to change the underlying df["Date"].

Next, create a plot of the wind speed over the course of the year. Then, create
an dual plot axes and use it to also plot humidity. Remember to add legends! 
The humidity will be plotted on the second axes.

"""

"""
EXERCISE 2

Remove the chart junk from the above dual axis

Long: remove the upper, left and right spines. Add a grid but make the y axis
grid lines invisible. Remove the tickmarks from the y axis. 

Hint: you will have to do this for both the original and twinx axes, so consider
using a loop
"""


"""
EXERCISE 3 (BONUS)

Create a histogram for the precipitation in the winter months and the summer months

Clarification: the winter months are November, December, January, Febuary. The summer is
May, June, July, and August.

Hint: 
    - You will have smaller dataframes for these months
    - Dataframes can use .dt to access datetime methods (similar to .str)
    - month is a datetime static attribute that contains the month as an integer
    - isin([1, 2, 3]) compares a value to a list of values - here it returns 
    true if it is in 1, 2, or 3,
"""