def dif_x(x, y): 
    return ((x**2)+(y**2))  

x0 = 0
y0 = 0
x = 0.4
h = 0.2

n = (int)((x - x0)/h) # Iteration number  
y = y0 

for i in range(n): 
    k1 = h * dif_x(x0, y) 
    k2 = h * dif_x(x0 + 0.5 * h, y + 0.5 * k1) 
    k3 = h * dif_x(x0 + 0.5 * h, y + 0.5 * k2) 
    k4 = h * dif_x(x0 + h, y + k3) 

    y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
    x0 = x0 + h 

print ('The value of y at x is:', y)