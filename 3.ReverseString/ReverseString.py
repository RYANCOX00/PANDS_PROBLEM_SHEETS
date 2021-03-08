# This program will read in a string and output it to the user in reverse with every second character present.
# Author: Ryan Cox


# Reading in a string from user.
inputString = input("Please enter a string: ")


# Function to print every second chartacter in reverse.
# Essentially stating there is no beginning, no end (i.e. start and end never defined) and step backwards in 2's. 
reverseString = inputString[::-2]


# Printing results of reverse string 
print(reverseString) 