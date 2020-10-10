# Write a program to solve the following system of linear equations by using Cramer’s Rule:
#                 27x + 6y – z = 85
#                 6x + 15y + 2z = 72
#                 x + y + 54z = 110

# a simple implementation using numpy
from numpy import linalg
 
A=[[2,-1,5,1],[3,2,2,-6],[1,3,3,-1],[5,-2,-3,3]]
B=[-3,-32,-47,49]
C=[[2,-1,5,1],[3,2,2,-6],[1,3,3,-1],[5,-2,-3,3]]
X=[]
for i in range(len(B)):
    for j in range(len(B)):
        # print(B[j])
        C[j][i]=B[j]
        if i>0:
            C[j][i-1]=A[j][i-1]
    X.append(round(linalg.det(C)/linalg.det(A),1))

print('w = {},x = {},y = {},z = {}'.format(X[0],X[1],X[2],X[3]))