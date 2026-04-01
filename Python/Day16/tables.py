#Table generator

table_num = int(input("Enter the multiplication table you want : "))
for i in range(1,10+1):
    print(f"{table_num} X {i} = {table_num*i}")

#Making range as dynamic
table_num = int(input("Enter the multiplication table you want : "))
n = int(input("Enter the maximum range : "))
for i in range(1,n+1):
    print(f"{table_num} X {i} = {table_num*i}")
