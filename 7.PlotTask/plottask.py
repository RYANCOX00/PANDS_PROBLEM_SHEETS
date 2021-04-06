# A program that plots 3 different lines on one line plot. 
# Each line has similar x values however they have a different equation to solve for y value of each line. 
# Author: Ryan Cox


# Importing numpy and matplotlib. 
import numpy as np 
import matplotlib.pyplot as plt

minRange = 0 # Defining the minimum parametre
maxRange = 4 # Defining the maximum parametre

fx = np.arange(minRange,maxRange)   # creating an array for the x value of f(x) line. Values are the range within the range parametres set above. 
fy = np.array([]) # creating empty array for y value of f(x) line. 

hx = np.arange(minRange,maxRange)
hy = np.array([])

gx = np.arange(minRange, maxRange)
gy = np.array([])


for x in fx: # loop the value of fx ie. the range of x values. 
    y = x # y is equal to x. 
    fy = np.append(fy,y) # Append y to the fy array.

for x in hx: # loop the value of hx ie. the range of x values. 
    y = x**2 # y is equal to x^2. 
    hy = np.append(hy,y) # append y to the hy array.

for x in gx: # loop the value of gx ie. the range of x values. 
    y = x**3 # y is equal to x^3. 
    gy = np.append(gy,y) # append y to the gy array.


# plotting f(x), h(x), and g(x). 
plt.plot(fx,fy, color='aqua', lw='2', label = 'f(x)') # ploting the f(x) line with adjusted color and line width.  Name this line 'f(x)'
plt.plot(hx,hy, color ='darkgreen',lw='4', label = 'h(x)') # similar adjustments made to h(x) line
plt.plot(gx,gy, color='hotpink', ls = '--', lw='2', label = 'g(x)') # ls is linestyle i.e. broken line. 
plt.legend() # adding a legend to the plot.
plt.title("Different Lines", fontsize=18, weight = "bold")  # Adding title to the plot with the font size and in bold font. 
plt.xlabel("x Axis", fontsize=12) # labeling  the x Axis with fontsize 12.
plt.ylabel("y Axis", fontsize=12) # labeling  the y Axis with fontsize 12.
plt.show()  # running the plot to show as an image.