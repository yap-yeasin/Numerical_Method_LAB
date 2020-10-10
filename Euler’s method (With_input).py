# Write a program to solve the following Differential Equation by using Euler’s method.
# dy / dx = 3x2 + 1, y (1) = 2. Compute y (2) taking h = 0.25.

def func( x, y ): 
	return (3*(x**2)+1) 	
x0 = 1
y0 = 2
h = 0.25
x = 2 
temp = -0
while x0 < x: 
	temp = y0 
	y0 = y0 + h * func(x0, y0) 
	x0 = x0 + h 
print("solution at x ~",x,' is ',y0) 