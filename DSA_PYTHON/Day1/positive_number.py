#Method 1: Using eval() function to take input as a list of positive numbers
'''
n = eval(input("Enter a list of positive numbers: "))
count = 0
for i in n:
    if i > 0:
        count += 1
if count > 0:
    print(f"The list contains {count} positive numbers.")
else:
    print("The list does not contain any positive numbers.")
'''
#Method 2: Using a loop to take input of positive numbers and count them
'''
n = int(input("Enter the number of numbers to input: "))
numbers = []
for i in range(1, n + 1):
   num = int(input(f"Enter {i} number: "))
   numbers.append(num)
count = 0
for num in numbers:
    if num > 0:
        count += 1
print("The list of numbers entered is:", numbers)
if count > 0:
    print(f"The list contains {count} positive numbers.")
else:
    print("The list does not contain any positive numbers.")
'''

#Method 3: Using list comprehension to take input as a list of positive numbers and count them
num = list(map(int, input("Enter a list of positive numbers separated by space: ").split()))
count = 0
for i in num:
    if i > 0:
        count += 1
if count > 0:
    print(f"The list contains {count} positive numbers.")
else:
    print("The list does not contain any positive numbers.")