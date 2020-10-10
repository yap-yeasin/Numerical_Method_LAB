# The following values of f (x) are given.
#                             x 1 2 3 4 5
#                             y = f(x) 1 8 27 64 125
# Write a program to find the first derivative and the second derivative of the function tabulated
# above at the point x = 1.

n = 5
x = [1,2,3,4,5] 
# h,u
h=x[1]-x[0]
# print(h)
x1=float(input('Enter the value of x - '))
u=(x1-x[0])/h
# print(u)

# Pro_Level
y = [[0 for i in range(n)] for j in range(n)] 
y[0][0] = 1
y[1][0] = 8
y[2][0] = 27
y[3][0] = 64 
y[4][0] = 125 
# print(y)
for i in range(1, n): 
    for j in range(n - i): 
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1] 
    #     print(y[j][i])
    # print('')

# Displaying the forward difference table 
# for i in range(n): 
#     print(x[i], end = "\t") 
#     for j in range(n - i): 
#         print(y[i][j], end = "\t") 
    # print('')

# print(y[0])  -> [2, 7, 12, 6, 0]

dif=(1/h)*(y[0][1]+(((2*u)-1)*y[0][2])/2+(((3*(u**2)-(6*u)+2))*y[0][3])/6+(((4*(u**3)-18*(u**2)+22*u-6)/24)*y[0][4])/24) 
dif2=(1/h**2)*( y[0][2] + (((6*(u)-6)*y[0][3])/6) + (((12*(u**2)-36*u+22 )*y[0][4])/24))
print(dif)
print(dif2)


