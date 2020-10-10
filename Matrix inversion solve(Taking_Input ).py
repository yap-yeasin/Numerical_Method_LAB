# Write a program to solve the following system of linear equations by using Matrix inversion
# method.
#                         x + y + z = 1
#                         x + 2y + 3z = 6
#                         x + 3y + 4z = 6

from numpy import *

m=int(input('Enter number of rows :'))
n=int(input('Enter number of columns :'))
A=zeros((m,n),dtype=int)
B=zeros((m,1),dtype=int)

l=len(A)
for i in range(l):
    for j in range(len(A[i])):
        v=int(input('C{}{} - '.format(i,j)))
        A[i][j]= v
l=len(B)
print('')
for c in range(l):
    for d in range(len(B[c])):
        vv=int(input('C{}{} - '.format(c,d)))
        B[c][d]= vv

x=linalg.solve(A,B)
l = x.tolist()

print('A is  ={}\n B is ={}\n  C is = {}'.format(l[0],l[1],l[2]))