# A program to perfom a calculation on a number inputted by a user.  
# The result will be saved to the list as a new number. 
# The calculation will be repeated (looped) on the new number until it reaches 1.
# Author: Ryan Cox

# Creating a list. 
numbersList = []

# Reading in a number from a user and adding this number to the list.
number = int(input("Enter an integer: "))
numbersList.append(number)


# Creating a loop until the latest number in the list reaches 1. 
while numbersList[-1] != 1:

# Performing different calculations the latest number of the list depending on whether they are even and odd numbers. 
    if numbersList[-1]%2 == 0:
       number = int(numbersList[-1]/2)
    else:
       number = int((numbersList[-1]*3)+1)

# Adding the calculated number to the list.     
    numbersList.append(number)


# Printing the list of numbers in numbersList.
print(numbersList)