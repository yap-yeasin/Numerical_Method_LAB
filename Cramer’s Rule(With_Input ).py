# Write a program to solve the following system of linear equations by using Cramer’s Rule:
#                 27x + 6y – z = 85
#                 6x + 15y + 2z = 72
#                 x + y + 54z = 110


# import numpy as np
from numpy import *

A = array([[27,6,1],[6,15,2],[1,1,54]])
print('Matrix_A-',A)
Dx = array([[85,72,110],[6,15,2],[1,1,54]])
print('Matrix_Dx-',Dx)
Dy = array([[27,6,1],[85,72,110],[1,1,54]])
print('Matrix_Dy-',Dy)
Dz = array([[27,6,1],[6,15,2],[85,72,110]])
print('Matrix_Dz-',Dz)

DIA=linalg.det(A)
DIDx=linalg.det(Dx)
DIDy=linalg.det(Dy)
DIDz=linalg.det(Dz)

print('The value of X is ={},Y is ={} Z is = {}'.format(DIDx/DIA,DIDy/DIA,DIDz/DIA))