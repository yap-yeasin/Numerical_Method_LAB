# Write a program to find the least square parabola y = a + bx + cx^2 for the following data
#             x -3 -1 1 3
#             y 15 5 1 5

from sympy import *

x=[-3, -1, 1, 3]
y=[15, 5, 1, 5]
n=len(y)

s2_x = [ i ** 2 for i in x]
s3_x = [ i ** 3 for i in x]
s4_x = [ i ** 4 for i in x]

# xy=[]
# for i,j in zip(x,y):
#     xy.append(i*j) 
xy=[i*j for i,j in zip(x,y) ]

# x2y=[]
# for i,j in zip(s2_x,y):
#     x2y.append(i*j) 
x2y=[i*j for i,j in zip(s2_x,y) ]

s_x=sum(x)
s_y=sum(y)
s_xy=sum(xy)
s_x2y=sum(x2y)
s_s2_x=sum(s2_x)
s_s3_x=sum(s3_x)
s_s4_x=sum(s4_x)

a,b,c = symbols('a,b,c')
eq1 = Eq(n*a+s_x*b+s_s2_x*c,s_y)

eq2 = Eq(s_x*a+s_s2_x*b+s_s3_x*c,s_xy)

eq3 = Eq(s_s2_x*a+s_s3_x*b+s_s4_x*c,s_x2y)

result = solve([eq1,eq2,eq3],(a,b,c))
print(result)
