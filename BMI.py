# A calculation to determine a users BMI 
# Author:  Ryan Cox


# Greeting the user
name = input ("Please enter your name: ")
print("Hello, " + name)


# Read in weight (kg) and height(cm), and converting the input as int variables
weight = int(input ("Enter you weight in kilograms: "))
height = int(input ("Enter your height in centimetres: "))


# Calculating the users BMI
BMI = int(weight/((height/100)**2))


# Telling the user their BMI
print ("Hi " + name + ". \tYour BMI is {}!".format(BMI))