# Programming and Scripting Weekly Problems <br />
**## Notes and references for weekly problems**
<br />

**# Task 1 - BMI**<br />
**File name:** bmi.py<br />

The program reads in the users height and weight and calculates the users BMI.  
<br />
Line 6 reads in the users weight in kilograms, coverts it to a float and saves the data as the variable "weight".  
<br />
Line 7 reads in the users height in centimetres, coverts this data to a float and stores it under the variable "height".  
<br />
Line 11 calculates the users BMI using (weight/((height/100)**2)). 
<br />
Line 15 rounds the float to 2 decimal places. 
<br />
Finally, line 20 tells the user their BMI. The output formats the float to output along side the string. <br />

**References**<br />
Python User Input, W3Schools, available at: https://www.w3schools.com/python/python_user_input.asp<br />
BMI Forumla, Ramsay health, available at: https://www.ramsayhealth.co.uk/weight-loss-surgery/bmi/bmi-formula<br />
Python round() Function, W3Schools, available at: https://www.w3schools.com/python/ref_func_round.asp<br />
Python String Formatting, W3Schools, available at: https://www.w3schools.com/python/python_string_formatting.asp<br />
<br />
<br />
<br />

**# Task 2 - Second String**
**File name:** secondstring.py

This program reads in a string and outputs it to the user in reverse with every second character present.

Line 6 reads in the string from the user using an input function.  This string is saved as the variable "inputString". 

Line 11 is a function to print every second chartacter of inputString in reverse - [::-2]. Essentially stating there is no beginning, no end (i.e. start and end never defined) and step backwards in 2's. The result is stored under the variable "reverseString".  Function[::-2] was obtained from W3Schools.

Line 15 prints the result of "reverseString". 

**References**
Python how to reverse string, W3 Schools, available at: https://www.w3schools.com/python/python_howto_reverse_string.asp.


**# Task 3**
**File name:** collatz.py

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
File name: weekday.py

The program uses a function obtained online to generate todays date and day of the week.  The day of the week is saved in the form of an integer range from [0:6].  We can then use an if statement to output a string based on the whether the day of the week is less than more greater than a certain threshold.  Integer 4, being Friday will be the upper threshold for weekdays. 

Line 7 initiates "from datetime import date" function.  This was obtained from https://www.programiz.com/python-programming/datetime/current-datetime. 

Line 13 first determines todays date from the date.today() function.  Also obtained from https://www.programiz.com/python-programming/datetime/current-datetime.  It then uses this date to determine what day of the week today is, .weekday(). The day of the week is saved under the variable weekNum as an integer, Monday (0) and Sunday(6). The weekday function was obtained from https://pythontic.com/datetime/datetime/weekday. 

Line 17 uses an if statement. If weekNum is equal to or less than 4 (Monday - Friday), then it is a weekday. 

Line 21 assumes that everything else is a weekend, i.e. 5 & 6. 




Week 6 
File name: 6.SquareRoot.py

The program  finds the square root of a number using Newtons Method. 

In line 10, I created the function squareRoot().  The first arguement is taken from the user in line 18. This is the squared number.  Arguement 2 is a random large number that will be used as the upper number in a range. Numbers in this range are used as an approximation in Newtons method. W3Schools was used for reference when creating functions, available: https://www.w3schools.com/python/python_functions.asp

Line 11 a for loop is created.  The for loop will use the range 1 - 1000 for approximation in Newtons method. The idea of using a for loop and range in Newtons method was sourced from: https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d 

Line 12 - The code is essentially 'guessing' the root until this equation is true. Using Newtons method, the square root is found when the equation is true.  The "root" as the variable being the same number for "root" in newtons method.  This equation was found at: https://www.school-for-champions.com/algebra/square_root_approx.htm#.YD2AAmj7RPa

Line 14, the number now found as the square root is returned out of the function. 

Line 18 reads a number in from the user.  This is the squared number. 
Line 19 calls the function and saving the float to one decimal place.

Line 23 prints the squared and square rooted number within a string merged through the format function. 



Week 7
File name: 7.Es.py

This program will read a file in from the command line and output the number of times the character "e" appears. 

Line 5 import the sys moudle to enable the user to input from the command line.  Understanding of this module was gained from: https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/

Line 8 uses the function argv() to read in an arguemen.  1 arguement was permitted. This argument will be the file, and it was saved under the variable "fileName. 

Line 11 creates a function for the reading in of the file, openFile().

Line 12 reads it in as read only. 

Line 13 - all the contents are read in and saved under the variable fileContents.  Empty brackets reads all the file. Note the contents is read in as a string.

Line 14 returns the variable fileConents out of the function. 

Line 17 is the start of the actual code.  This line initiates the function and saves what is returned out i.e. fileContents to a variable outside the function, also called fileContents. 

Line 18 counts the incidences of the character "e" in fileContents and saves this figure as the variable "count".  This idea for the count function for strings was obtained from https://www.w3schools.com/python/ref_string_count.asp

Line 20 prints count. 