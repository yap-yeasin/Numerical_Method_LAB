# Write a program to find the least square line y = a + bx for the following data
#                 x -2 1 0 1 2
#                 y 1 2 3 3 4

lix=[2,10,26,61]
liy=[600,500,400,350]
n=len(liy)

sq_lix = [ i ** 2 for i in lix]
# print(sq_lix)

xy=[]
for i,j in zip(lix,liy):
    xy.append(i*j) 
sum_lix=sum(lix)
sum_liy=sum(liy)
sum_xy=sum(xy)
sum_sq_lix=sum(sq_lix)
# print(sq_lix)
# print(xy)
# print(sum_lix)
# print(sum_liy)
# print(sum_sq_lix)
# print(sum_xy)
d=n*sum_sq_lix - (sum_lix)**2
a=round(((sum_liy*sum_sq_lix)-(sum_lix*sum_xy))/d,5)
b=round(((n*sum_xy)-(sum_lix*sum_liy))/d,5)

print('The value of a is {} & b is {}'.format(a,b))