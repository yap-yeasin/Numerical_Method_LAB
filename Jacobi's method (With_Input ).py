# Write a program to solve the following system of linear equations by using Jacobi's method.
#                         83x + 11y - 4z = 95
#                         3x + 8y + 29z = 71
#                         7x + 52y + 13z = 104


from numpy import *
import numpy as np
from numpy.linalg import inv

n= int(input(' Value for Iteration - '))
a = array([[83,11,-4],[3,8,29],[7,52,13]])
b = array([95,71,104])

g=array([0.0,0.0,0.0])

u=triu(a,1)
l=tril(a,-1)
d=diagflat(diag(a))
ind= inv(d)
LU= -l-u

for i in range(n):
    LU_D_B=dot(LU,g)+b
    g=dot(ind,LU_D_B)
print('Iteration({})  Solution x1,x2,x3 ={}'.format(i+1,g))
