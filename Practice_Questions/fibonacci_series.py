#fibonocci series
user_in = int(input("Enter the limit : "))
num_1 = 0
num_2 =1
print(num_1, num_2, end=" ")
for i in range(user_in+1):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3,end =" ")
