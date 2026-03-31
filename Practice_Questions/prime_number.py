
#To find wheather a number is prime or not

num = int(input("Enter a number : "))
count = 0
for j in range(1,num+1):
    if num % j == 0:
        count+=1
    if count > 2:
        break
if count == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


#to check prime numbers until specific range

num = int(input("Enter the range of numbers : "))
for i in range(1,num+1):
    count = 0
    for j in range(1,i+1):
        if i % j ==0:
            count+=1
    if count == 2:
        print(f"{i} is a prime number")
    else:
        print(f"{i} is not a prime number")


#To check prime numbers in list

num=[1057,197,9,86,17673]
for i in num:
    count=0
    for j in range(1,i+1):
        if i % j == 0:
            count+=1
    if count == 2:
        print(f"{i} is a prime number")
    else:
        print(f"{i} is not a prime number")


































