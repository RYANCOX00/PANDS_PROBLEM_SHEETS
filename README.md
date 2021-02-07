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