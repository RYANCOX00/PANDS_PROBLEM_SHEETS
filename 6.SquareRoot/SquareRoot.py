# A program that finds the square root of a number using Newtons Method.
# Author: Ryan Cox

#REF:  https://www.school-for-champions.com/algebra/square_root_approx.htm#.YD2AAmj7RPa
#REF:  https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
#REF:  https://www.w3schools.com/python/python_functions.asp


# Creating a function squareRoot to be recalled later.
def squareRoot(squared, root=1000): # Arguement 1 parameter from code below. Arguement 2 parameter set to 1000.
    for i in range(root): # The for loop will use the range 1 - 1000 to approximate in Newtons method. 
        root = ((root + (squared/root))/2)  #'Guessing' the root until this equation is true.

    return  root # It will return the correct square root.


# Running the function with the parameter read in from the user.
squared = float(input("Please enter a positive number: ")) 
root = round(squareRoot(squared), 1) # Recalling the function and saving the float to one decimal place.


# Outputting the squared and square rooted number
print("The square root of {} is approx. {}.".format(squared,root)) 