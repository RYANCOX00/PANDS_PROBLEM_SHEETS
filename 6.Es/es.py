# A program that will read a file on the command line and output the number of times the character "e" & "E" appears. 
# Author: Ryan Cox


import sys  # Importing the sys module to read in file from command line.
            

fileName = sys.argv[1] # Reading in 1 arguement from the command line and saving it as "fileName"


def openFile(): # Creating a function to read in a file. 
    with open(fileName, "rt") as f: # File is on read only. 
        fileContents = f.read() # Reading in the entire file. 
    return fileContents # Return the contents


fileContents = openFile() # Saving the contents of the file under the "fileContents" variable
count = fileContents.count("e")     # Count the occurances the character "e" appears in the variable (string). 
count2 = fileContents.count("E") # I am also running the count of uppercase "E"
count3 = count + count2  # Adding both counts together and saving as count3. 

print(count) # Printing count3.