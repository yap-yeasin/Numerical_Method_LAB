# Write a program to solve the following system of linear equations by using Gauss-Jordan Elimination method.
#                     x + 2y + z = 8
#                     2x + 3y + 4z = 20
#                     4x + 3y + 2z = 16

from numpy import *

m=int(input('Enter number of rows :'))
n=int(input('Enter number of columns :'))

A=zeros((m,n+1),dtype=int)
# B=zeros((m,1),dtype=int)

l=len(A)
for i in range(l):
    for j in range(len(A[i])):
        # v=int(input('enter the matrix element- ',))
        v=float(input( 'C'+str(i+1)+ str(j+1)+'='))
        A[i][j]= v
# l=len(B)
# for c in range(l):
#     for d in range(len(B[c])):
#         vv=int(input('enter the next matrix element- ',))
#         B[c][d]= vv
# print(A)
# print(B)

for i in range(n):
    if A[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
        
    for j in range(n):
        if i != j:
            ratio = A[j][i]/A[i][i]
            for k in range(n+1):
                A[j][k] = A[j][k] - ratio * A[i][k]

# Obtaining Solution
x = zeros(n)
for i in range(n):
    x[i] = A[i][n]/A[i][i]
# print(x)

# Displaying solution
print('\nRequired solution is: ')
for i in range(n):
    print('X'+str(i)+'='+str(x[i]))
# print('X = {},Y ={},Z={}'.format(x[0],x[1],x[2]))