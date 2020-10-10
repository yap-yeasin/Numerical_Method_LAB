# The following values of f (x) are given.
#                             x 1 2 3 4 5
#                             y = f(x) 1 8 27 64 125
# Write a program to find the first derivative and the second derivative of the function tabulated
# above at the point x = 1.


# Baby level coding
n = 5
x = [1,2,3,4,5] 
y = [2,9,28,65,126]
# h,u
h=x[1]-x[0]
# print(h)
x1=float(input('Enter the value of x - '))
u=(x1-x[0])/h
# Calculating the forward difference table 
y1=[]
for j in range(len(y)-1): 
    y1.append(y[j + 1]- y[j])
# print(y1)
y2=[]
for j in range(len(y1)-1 ): 
    y2.append(y1[j + 1]- y1[j])
# print(y2)
y3=[]
for j in range(len(y2)-1): 
    y3.append(y2[j + 1]- y2[j])
# print(y3)
y4=[]
for j in range(len(y3)-1): 
    y4.append(y3[j + 1]- y3[j])
# print(y4)
# f(x1)
# y = [2,9,28,65,126]
# y1= [7, 19, 37, 61]
# y2= [12, 18, 24]      
# y3= [6, 6]
# y4= [0]

dif=(1/h)*(y1[0]+(((2*u)-1)*y2[0])/2+(((3*(u**2)-(6*u)+2))*y3[0])/6+(((4*(u**3)-18*(u**2)+22*u-6)/24)*y4[0])/24) 
dif2=(1/h**2)*( y2[0] + (((6*(u)-6)*y3[0])/6) + (((12*(u**2)-36*u+22 )*y4[0])/24))
print(dif)
print(dif2)
