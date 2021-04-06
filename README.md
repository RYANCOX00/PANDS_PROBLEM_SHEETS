# Programming and Scripting Weekly Problems <br />
The purpose of this repository is for pushing weekly tasks for the Programing and Scripting module at GMIT. <br />
<br />

### Notes and references for weekly problems <br />
Below is a summary and breakdown of each weekly task. Also included are the references used for solving these problems. <br />
<br />

## Task 1 - BMI <br />
**File name:** bmi.py<br />
<br />

**Summary:** The program reads in the users height and weight and calculates the users BMI.  <br />
<br />
Line 6 reads in the users weight in kilograms, coverts it to a float and saves the data as the variable "weight".  <br />
<br />
Line 7 reads in the users height in centimetres, coverts this data to a float and stores it under the variable "height".  <br />
<br />
Line 11 calculates the users BMI using (weight/((height/100)**2)). <br /> 
<br />
Line 15 rounds the float to 2 decimal places. <br />
<br />
Finally, line 20 tells the user their BMI. The output is a float that has been formatted within a string. <br />
<br />

**References**<br />
Python User Input, W3Schools, available at: https://www.w3schools.com/python/python_user_input.asp<br />
BMI Forumla, Ramsay health, available at: https://www.ramsayhealth.co.uk/weight-loss-surgery/bmi/bmi-formula<br />
Python round() Function, W3Schools, available at: https://www.w3schools.com/python/ref_func_round.asp<br />
Python String Formatting, W3Schools, available at: https://www.w3schools.com/python/python_string_formatting.asp<br />
<br />
<br />

## Task 2 - Second String<br />
**File name:** secondstring.py<br />
<br />

**Summary:** This program reads in a string and outputs it to the user in reverse with every second character present.<br />
<br />
Line 6 reads in the string from the user using an input function.  This string is saved as the variable "inputString". <br />
<br />
Line 11 is a function to print every second chartacter of inputString in reverse - [::-2]. Essentially stating there is no beginning, no end (i.e. start and end never defined) and step backwards in 2's. The result is stored under the variable "reverseString".<br />
<br />
Line 15 prints the result of "reverseString". <br />
<br />

**References**<br />
Python User Input, W3Schools, available at: https://www.w3schools.com/python/python_user_input.asp<br />
Python how to reverse string, W3 Schools, available at: https://www.w3schools.com/python/python_howto_reverse_string.asp.<br />
<br />
<br />

## Task 3 - Collatz <br />
**File name:** collatz.py <br />
<br />

**Summary:** This program reads in a number from a user and saves it to an empty list. The initial number the user inputs is put through a specific calculation depending on whether it is odd or even. The outcome is added to numbersList. The latest number of the list is then put through the same calculation.  This calculation is an if statement within a loop.  The latest number in the list is put through this calculation until the latest number in the list equals to 1. Finally, the full contents of numbersList is printed. <br />
<br />
Line 7 creates an empty list and saves it as a variable 'numbersList'.<br />
<br />
Line 10 reads in a number from a user as an integer and saves it under the variable 'number'<br />
<br />
Line 11 adds this number to the list, 'numbersList'. <br />
<br />
Line 15 creates a loop with a condition that it will run until latest version of 'number' equals to 1. <br />
<br />
Line 18 takes the latest number in 'numbersList' if it is an even number. Using an If Statement, it preforms a specific calculation on it when 'number' equals to an even number.<br /> 
<br />
Line 21 also takes the latest number in 'numbersList' if it is odd. Using the 'else' function, it preforms a specific calculation on all other numbers i.e. odd numbers. <br />
<br />
Line 24 add the new version of 'number' as defined under line 18 or 21 and adds this as the latest number of 'numbersList'. The loop is repeated until the lastest number of 'numberList' equals to 1. <br />
<br />
Line 28 prints the contents of 'numbersList' once the latest number equals to 1. <br />
<br />

**References** <br />
Python User Input, W3Schools, available at: https://www.w3schools.com/python/python_user_input.asp<br />
Python While Loops, W3Schools, available at: https://www.w3schools.com/python/python_while_loops.asp<br />
Python - Access List Items, W3Schools, available at: https://www.w3schools.com/python/python_lists_access.asp <br />
Python If ... Else, W3Schools, available at: https://www.w3schools.com/python/python_conditions.asp<br />
Python List append() Method, W3Schools, available at: https://www.w3schools.com/python/ref_list_append.asp<br />
<br />
<br />

## Task 4 - Weekday <br />
**File name:** weekday.py <br />
<br />

**Summary:** The program uses a function obtained online to generate todays date and day of the week.  The day of the week is saved in the form of an integer range from [0:6].  We can then use an if statement to output a string based on the whether the day of the week is less than more greater than a certain threshold.  Integer 4, being Friday will be the upper threshold for weekdays. <br />
<br />
Line 7 initiates "from datetime import date" function.  <br />
<br />
Line 13 first determines todays date from the date.today() function.  It then uses this date to determine what day of the week today is - .weekday(). The day of the week is saved under the variable weekNum as an integer, Monday (0) and Sunday(6). <br />
<br />
Line 17 uses an if statement. If weekNum is equal to or less than 4 (Monday - Friday), then it is a weekday. <br />
<br />
Line 21 assumes that everything else is a weekend, i.e. 5 & 6. <br />
<br />

**References** <br />
How to get current date and time in Python?, Programiz, available at: https://www.programiz.com/python-programming/datetime/current-datetime<br />
Weekday() Method Of Datetime Class In Python, Puthonic, available at: https://pythontic.com/datetime/datetime/weekday<br />
Python If ... Else, W3Schools, available at: https://www.w3schools.com/python/python_conditions.asp<br />
<br />
<br />

## Task 5 -  Square Root <br />
**File name:** squareRoot.py<br />
<br />

**Summary:** The program  finds the square root of a number using Newtons Method. <br />
<br />
In line 6, I created the function squareRoot().  The first arguement is taken from the user in line 18. This is the squared number.  Arguement 2 is a random large number that will be used as the upper number in a range. Numbers in this range are used as an approximation in Newtons method. <br />
<br />
Line 7 a for loop is created.  The for loop will use the range 1 - 1000 for approximation in Newtons method.<br />
<br />
Line 8 - The code is essentially 'guessing' the root until this equation is true. Using Newtons method, the square root is found when the equation is true.  The "root" as the variable being the same number for "root" in newtons method. <br />
<br />
Line 10, the number now found as the square root is returned out of the function. <br />
<br />
Line 14 reads a number in from the user.  This is the squared number. <br />
<br />
Line 15 calls the function and saving the float to one decimal place.<br />
<br />
Line 19 prints the squared and square rooted number within a string merged through the format function. <br />

**References**<br />
Python Functions, W3Schools, available at: https://www.w3schools.com/python/python_functions.asp<br />
Python For Loops, W3Schools, available at: https://www.w3schools.com/python/python_for_loops.asp<br />
Newton Square Root Method in Python, Sıddık Açıl, available at: https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d <br />
Newton's Square Root Approximation, School for Champions, available at: https://www.school-for-champions.com/algebra/square_root_approx.htm#.YD2AAmj7RPa<br />
Python User Input, W3Schools, available at: https://www.w3schools.com/python/python_user_input.asp<br />
Python String Formatting, W3Schools, available at: https://www.w3schools.com/python/python_string_formatting.asp<br />
Python round() Function, W3Schools, available at: https://www.w3schools.com/python/ref_func_round.asp <br />
<br />
<br />

## Task 6 - Es <br />
**File name:** es.py <br />
<br />

**Summary:** This program will read a file in from the command line and output the number of times the characters "e" & "E" appears. <br />
<br />
Line 5 import the sys moudle to enable the user to input from the command line.  <br />
<br />
Line 8 uses the function argv() to read in an arguement.  1 arguement was permitted in addition to the python file name. This additional argument will be the text file, and it was saved under the variable "fileName.  <br />
<br />
Line 11 creates a function for the reading in of the file, openFile().<br />
<br />
Line 12 reads it in as read only. <br />
<br />
Line 13 - all the contents are read in and saved under the variable fileContents.  Empty brackets reads all the file. Note the contents is read in as a string.<br />
<br />
Line 14 returns the variable fileConents out of the function.<br />
<br />
Line 17 is the start of the actual code.  This line initiates the function and saves what is returned out i.e. fileContents to a variable outside the function, also called fileContents. <br />
<br />
Line 18 counts the incidences of the character "e" in fileContents and saves this figure as the variable "count". <br />
<br />
Line 19 counts the indcidences of the character "E" (uppercase also) using the same functions also line 18.<br />
<br />
Line 20 adds both counts together.<br />
<br />
Line 22 prints count. <br />

**References** <br />
How to use sys.argv in Python, Geeks for Geeks, available at: https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/<br />
Python File Open, W3Schools, available at: https://www.w3schools.com/python/python_file_handling.asp<br />
Python Functions, W3Schools, available at: https://www.w3schools.com/python/python_functions.asp<br />
Python String count() Method, W3Schools, available at: https://www.w3schools.com/python/ref_string_count.asp<br />
<br />
<br />

## Task 7 - Plot Task <br />
**File name:** plottask.py <br />
<br />

**Summary:** # A program that plots 3 different lines on one line plot. Each line has similar parametres however they have a different equations.<br />
<br />
Line 7 and line 8 import numpy and matplotlib respectively. <br />
<br />
Line 10 and line 11 defines the minrange and maxrange of the x value for each line.  These values were taken from the question. <br />
<br />
Line 13 creates a numpy array for the x values of the f(x) line.  The contents of this array are the whole numbers between the defined min and max ranges at line 10 and 11. The numpy function .arange() was used to fill the array contents.<br />
<br />
Line 14 creates a numpy array for the y values of the f(x) line. These values will be found later between lines 23 and 25. The formula was provided in the question for the y values.<br />
<br />
Line 16 creates a numpy array for the x values of the h(x) line. The contents of this array are the whole numbers between the defined min and max ranges at line 10 and 11. The numpy function .arange() was used to fill the array contents.<br />
<br />
Line 17 creates a numpy array for the y values of the h(x) line. These values will be found later between lines 27 and 29. The formula was provided in the question for the y values.<br />
<br />
Line 19 creates a numpy array for the x values of the g(x) line. The contents of this array are the whole numbers between the defined min and max ranges at line 10 and 11. The numpy function .arange() was used to fill the array contents.<br />
<br />
Line 20 creates a numpy array for the y values of the g(y) line. These values will be found later between lines 31 and 33. The formula was provided in the question for the y values.<br />
<br />
Line 23 - 25 creates the y values of the f line by way of a for loop.  We are told that y values are equal to x values. <br />
<br />
Line 27 - 29 creates the y values of the h line by way of a for loop.  We are told that y values are equal to x values to the power of 2. <br />
<br />
Line 31 - 33 creates the y values of the g line by way of a for loop.  We are told that y values are equal to x values to the power of 3. <br />
<br />
Line 37 - 39 plots the f, h and g line.  Colors, line width and line style are adjusted.  Each line is given a label. <br />
<br />
Line 40 plots the legend of the lines.<br />
<br />
Line 41 plots the titles of the plot.<br />
<br />
Line 42 and 43 plots the x and y axis repectively.<br />
<br />
Line 44 shows the plot. I then saved this in the repository seperately.  <br />

**References** <br />
NumPy Tutorial, W3Schools, available at: https://www.w3schools.com/python/numpy/default.asp<br />
NumPy Creating Arrays, W3Schools, available at: https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp<br />
Import Matplotlib, w3Schools, available at: https://www.w3schools.com/python/matplotlib_getting_started.asp<br />
Range Arguments of np.arange(), Real Python, available at: https://realpython.com/how-to-use-numpy-arange/#range-arguments-of-nparange<br />
Python For Loops, W3Schools, available at: https://www.w3schools.com/python/python_for_loops.asp<br />
numpy.append, Tutorials Point, available at: https://www.tutorialspoint.com/numpy/numpy_append.htm<br />
Matplotlib Line, W3Schools, available at: https://www.w3schools.com/python/matplotlib_line.asp<br />