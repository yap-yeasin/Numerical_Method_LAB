# Write a program to find the determinant of a m*n matrix.

from numpy import *
m=int(input('Enter number of rows :'))
n=int(input('Enter number of columns :'))
#  zeros function ja 2D zero return kore (Data type f)
a=zeros((m,n),dtype=int)
# print(a)
# ekhne len rows count kore
l=len(a)
for i in range(l):
    for j in range(len(a[i])):
        v=int(input('enter the matrix element',))
        a[i][j]= v

# for i in range(l):
#     for j in range(len(a[i])):
#         print(a[i][j])

print(a)        
print ("the determinant of a M*N matrix =",linalg.det(a)) 