# PANDS_PROBLEM_SHEETS
Referneces and notes for weekly problems






Week 2
The program reads in the users height and weight and calculates the users BMI.  

Line 6 asks the user the name and stores this string under the variable "name". 

Line 7 greets the user.   

Line 11 reads in the users weight in kilograms, coverts it to a float and saves the data as the variable "weight".  

Line 12 reads in the users height in centimetres, coverts this data to a float and stores it under the variable "height".  

Line 16 calculates the users BMI using (weight/((height/100)**2)). 

Line 20 rounds the float to 2 decimal places. 
Finally, line 25 tells the user their BMI. 






Week 3
This program reads in a string and outputs it to the user in reverse with every second character present.

Line 6 reads in the string from the user using an input function.  This string is saved as the variable "inputString". 

Line 11 is a function to print every second chartacter of inputString in reverse - [::-2]. Essentially stating there is no beginning, no end (i.e. start and end never defined) and step backwards in 2's. The result is stored under the variable "reverseString".  Function[::-2] was obtained from W3Schools, available at https://www.w3schools.com/python/python_howto_reverse_string.asp.

Line 15 prints the result of "reverseString". 





Week 4
This program reads in a number from a user and saves it to an empty list. The initial number the user inputs, as the first number in the list, is put through a specific calculation depending on whether it is odd or even. This number is then put through the same calculation.  This calculation, as an if statement, is a statement within a loop.  The latest number in the list is put through this calculation until the latest number in the list equals to 1.

Line 7 creates an empty list and saves it as a variable 'numbersList'.

Line 10 reads in a number from a user as an integer and saves it under the variable 'number'

Line 11 adds this number to the list, 'numbersList'. 

Line 15 creates a loop with a condition that it will run until latest version of 'number' equals to 1. 

Line 18 takes the latest number in 'numbersList'. Using an If Statement, it preforms a specific calculation on it when 'number' equals to an even number. 

Line 21 also takes the latest number in 'numbersList'. Using the 'else' function, it preforms a specific calculation on all other numbers i.e. odd numbers. 

Line 24 add the new version of 'number' as defined under line 18 or 21 and adds this as the latest number of 'numbersList'. The loop is repeated until the lastest number of 'numberList' equals to 1. 

Line 28 prints the contents of 'numbersList' once the latest number equals to 1. 





Week 5
The program uses a function obtained online to generate todays date and day of the week.  The day of the week is saved in the form of an integer range from [0:6].  We can then use an if statement to output a string based on the whether the day of the week is less than more greater than a certain threshold.  Integer 4, being Friday will be the upper threshold for weekdays. 

Line 7 initiates "from datetime import date" function.  This was obtained from https://www.programiz.com/python-programming/datetime/current-datetime. 

Line 13 first determines todays date from the date.today() function.  Also obtained from https://www.programiz.com/python-programming/datetime/current-datetime.  It then uses this date to determine what day of the week today is, .weekday(). The day of the week is saved under the variable weekNum as an integer, Monday (0) and Sunday(6). The weekday function was obtained from https://pythontic.com/datetime/datetime/weekday. 

Line 17 uses an if statement. If weekNum is equal to or less than 4 (Monday - Friday), then it is a weekday. 

Line 21 assumes that everything else is a weekend, i.e. 5 & 6. 