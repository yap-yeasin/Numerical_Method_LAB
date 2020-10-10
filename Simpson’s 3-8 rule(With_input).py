# Write a program to calculate the approximate area under the curve y = ∫1 x / (1+x) by using
# Simpson’s 3/8 rule

from math import *
def y( x ):
    return (x/(1+x))
a = 0
b = 1
n = 6

h = (b - a) / n  
s = (y(a) + y(b)) 
i = 1
while i < n:
    if i % 2 != 0:
        s+= 4 * y(a + i * h)
        i+=1
    else:
        s+= 2 * y(a + i * h)
        i+=1
print('solution - ',(3*h/8) * s)