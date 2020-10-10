# Write a program to solve the following system of linear equations by using Gauss-Seidel method.
#             10x1 + x2 + x3 = 12
#             2x1 + 10x2 + x3 = 13
#             2x1 + 2x2 + 10x3 = 14

from numpy import *
import numpy as np
from numpy.linalg import inv

n= 20
a=array([[2,1,1],[3,5,2],[2,1,4]])
b=array([5,15,8])

g=array([0.0,0.0,0.0])

# Main law for this 
# x^(k+1)=inv(l+d)[-ux^k + b]
# https://www.geeksforgeeks.org/gauss-seidel-method/

u=triu(a,1)
l_d=tril(a,0)
ind= inv(l_d)


for i in range(n):
    MU_b= -dot(u,g)+b
    g=dot(ind,MU_b)
    # print(i,np.round(g,5))
    print('Iteration({})  Solution x1,x2,x3 ={}'.format(i+1,g))
