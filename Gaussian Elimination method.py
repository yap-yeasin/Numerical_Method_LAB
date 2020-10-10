# Write a program to solve the following system of linear equations by using Gaussian Elimination method.
#             2x + y + z = 10
#             x + 4y + 9z = 16
#             3x + 2y + 3z = 18

from sympy import Matrix
A= Matrix([[2,1,1,10],[3,2,3,18],[1,4,9,16]])
#Creating Upper triangle & Lower triangle
L,U,O =A.LUdecomposition()
# print(U)

Z=U[11]/U[10]
Y=(U[7]-U[6]*Z)/U[5]
X=(U[3]-U[2]*Z-U[1]*Y)/U[0]
print('Value of x= {},y= {},z= {}'.format(X,Y,Z))
