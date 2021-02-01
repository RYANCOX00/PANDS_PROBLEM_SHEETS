# A calculation to determine a users BMI 
# Author:  Ryan Cox


# Reading in the users name and greeting the user 
name = input ("Please enter your name: ")
print("Hello, " + name)


# Reading in weight (kg) and height(cm) as variables, and converting these variables to ints
weight = int(input ("Enter you weight in kilograms: "))
height = int(input ("Enter your height in centimetres: "))


# Calculating the users BMI and saving under BMI variable.
# Converting to an int incase we wish to work with this number later.
BMI = int(weight/((height/100)**2))


# Adding the variables to the output using .format. 
# Telling the user their BMI. 
print (name + ", your BMI is {}.".format(BMI))