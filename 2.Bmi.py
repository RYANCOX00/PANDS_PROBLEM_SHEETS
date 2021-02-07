# A calculation to determine a users BMI 
# Author:  Ryan Cox


# Reading in the users name and greeting the user 
name = input ("Please enter your name: ")
print("Hello, " + name)


# Reading in weight (kg) and height(cm) as variables, and converting these variables to floats
weight = float(input ("Enter you weight in kilograms: "))
height = float(input ("Enter your height in centimetres: "))


# Calculating the users BMI and saving under BMI variable.
BMI = float(weight/((height/100)**2))


# Rounding BMI to 2 decimal places.  Source: (Kite.com, 2021)
BMI = round(BMI, 2)


# Adding the variables to the output using format. 
# Telling the user their BMI. 
print (name + ", your BMI is {}.".format(BMI))