# Write a program to calculate the approximate area under the curve y = ∫/2 esinx dx by using
# Simpson’s 1/3 rule

from math import *
def y( x ):
    return (exp(sin(x)))
a = 0
b = pi/2
n = 4
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
print('solution - ',(h / 3) * s)


