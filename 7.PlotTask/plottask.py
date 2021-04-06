import numpy as np 
import matplotlib.pyplot as plt

minRange = 0
maxRange = 4

fx = np.arange(minRange,maxRange)   # x value is within the range parametres set above. 
                                    # np.arange obtained from https://realpython.com/how-to-use-numpy-arange/#range-arguments-of-nparange
fy = np.array([]) # creating empty array for y value. 

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
plt.plot(fx,fy, color='aqua', lw='2', label = 'f(x)') # colors obtianed from https://matplotlib.org/stable/gallery/color/named_colors.html
plt.plot(hx,hy, color ='darkgreen',lw='4', label = 'h(x)') # lw is linewidth.  label referes to name of the line. 
plt.plot(gx,gy, color='hotpink', ls = '--', lw='2', label = 'g(x)') # ls is linestyle i.e. broken line. 
plt.legend() # adding a legend
plt.title("Different Lines", fontsize=18, weight = "bold")  # adding title to the plot. Weight obtained from https://matplotlib.org/stable/tutorials/text/text_props.html
plt.xlabel("x Axis", fontsize=12) # labeling 
plt.ylabel("y Axis", fontsize=12)
plt.show()  