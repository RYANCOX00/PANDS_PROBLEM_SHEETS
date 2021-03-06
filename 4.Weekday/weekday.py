# A program to tell a user whether it is a weekday or a weekend. 
# Author: Ryan Cox


# importing the datetime. 
from datetime import date


# Getting todays date from date.today(). See readme for reference. 
# Also the day of the week returned as an integer by weekday().
# The current day of the week as an integer saved under weekNum, i.e. Monday = 0,  Tuesday = 1. 
weekNum = date.today().weekday()


# If weekNum is equal to or less than 4 (Monday - Friday), then it is a weekday. 
if weekNum <= 4:
    print("Yes, unfortunately today is a weekday.")

#Otherwise it is a weekend. 
else:("It is the weekend, yay!") 