# Write a program to calculate the approximate area under the curve y = ∫5 log10 x dx
# by using trapezoidal rule

from math import *
def y( x ): 
	# Declaring the function 
	# f(x) = log10(x)
	return (log10(x)) 
	
# Function to evalute the value of integral 
def trapezoidal (a, b, n): 
	# Grid spacing 
	h = (b - a) / n 
	# Computing sum of first and last terms 
	# in above formula 
	s = (y(a) + y(b)) 
	# Adding middle terms in above formula 
	i = 1
	while i < n: 
		s += 2 * y(a + i * h) 
		i += 1	
	# h/2 indicates (b-a)/2n. 
	# Multiplying h/2 with s. 
	return ((h / 2) * s) 

# Driver code to test above function 
# Range of definite integral 
x0 = 1
xn = 5

# Number of grids. Higher value means 
# more accuracy 
n = 8
print ("Value of integral is ", trapezoidal(x0, xn, n)) 


