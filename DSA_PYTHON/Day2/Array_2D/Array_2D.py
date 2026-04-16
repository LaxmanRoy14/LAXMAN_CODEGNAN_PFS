#Method-1
# row = int(input("Enter the number of rows : "))
# columns = int(input("Enter the number of columns : "))
# a=[]
# for i in range(row):
#     temp=[]
#     for j in range(columns):
#         num = int(input(f"Enter the number for index [{i}],[{j}]"))
#         temp.append(num)
#     a.append(temp)
# print(a)

#Method-2
row = int(input("Enter the number of rows : "))
a=[]
for i in range(row):
    a.append(list(map(int,input().split())))

print("Before Traversal : ",a)

#Traversing 2D Array
for i in a:
    for j in i:
        print(j)