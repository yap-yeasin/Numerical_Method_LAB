n = 5
x = [1,2,3,4,5] 
y = [2,9,28,65,126]
  
# Calculating the forward difference 
# table 
# Baby level
y1=[]
for j in range(len(y)-1): 
    y1.append(y[j + 1]- y[j])
print(y1)

y2=[]
for j in range(len(y1)-1 ): 
    y2.append(y1[j + 1]- y1[j])
print(y2)

y3=[]
for j in range(len(y2)-1): 
    y3.append(y2[j + 1]- y2[j])
print(y3)

y4=[]
for j in range(len(y3)-1): 
    y4.append(y3[j + 1]- y3[j])
print(y4)

# Pro_Level
# y = [[0 for i in range(n)] for j in range(n)] 
# y[0][0] = 2 
# y[1][0] = 9
# y[2][0] = 28
# y[3][0] = 65 
# y[4][0] = 126 
# print(y)
  
# for i in range(1, n): 
#     for j in range(n - i): 
#         y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

# # Displaying the forward difference table 
# for i in range(n): 
#     print(x[i], end = "\t") 
#     for j in range(n - i): 
#         print(y[i][j], end = "\t") 
#     print('')