# Write a program to solve the following system of linear equations by using Matrix inversion
# method.
#                         x + y + z = 1
#                         x + 2y + 3z = 6
#                         x + 3y + 4z = 6

# import numpy as np
from numpy import *
# Ax=B
#x=(A^-1).B
A = array([[1,1,1],[1,2,3],[1,3,4]])
print(A)
B=array([1,6,6])
x=linalg.solve(A,B)
print(type(x))
# numpy.ndarray to list
l = x.tolist()

print('The value of X is ={},Y is ={} Z is = {}'.format(l[0],l[1],l[2]))