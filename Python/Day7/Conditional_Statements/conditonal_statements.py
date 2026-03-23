'''
if statement
if-else statement
if-elif-else statement

code Q

'''

#if statement
'''
-->if statement

--> This (if statement) is used to check any condition, if the condition becomes true,
then it will enter inside the condition (if statement)

#Example 1:
age = int(input("Enter your age : "))
if age >= 18:
    print("Your age is 18 or above")


#Example 2:
student_att = int(input("Please enter your semester attendance : "))

if student_att >= 75:
    print("You can directly sit in the semester exams")

if student_att <= 75:
    print("You cannot directly sit in the semester exams")

#Example 3
price = int(input("Enter the price : "))
budget = int(input("Enter the budget : "))

if price > budget:
    print("Cannot effort the price")

#Example 4
grade = float(input("Enter CGPA : "))
if grade > 7.5:
    print("You are eligible for Placements")
'''

#if-else statement
'''
if-else statement
--> This also called as fall back statement which only executes when the if statement becomes false

#Example 1
age = int(input("Enter your age : "))
if age >= 18:
    print("You can vote")
else:
    print(f"You cannot vote. You can vote after {18-age} years")

#Example 2
total_amount = int(input("Enter the total shopping money : "))
if total_amount >= 149:
    print("No delivery cost applicable. Free delivery")
else:
    print(f"Add {149 - total_amount} rupees worth of items to your cart for free delivery")

#Example 3
price = int(input("Enter the price : "))
budget = int(input("Enter the budget : "))

if price > budget:
    print(f"You cannot effort the price. Your budget is less by {price - budget}")
else:
    print("You can buy the product")
'''

#if-elif-else
'''
--> if-elif-else statement (if + else)
--> In the elif part, I can check one more condition


#Example 1:

student_marks = int(input("Enter your marks : "))

if student_marks >= 90:
    print("You got A+ grade")
    
elif student_marks >= 74 and student_marks < 90:
    print("You got A grade")

elif student_marks >= 60 and student_marks < 75:
    print("You got B+ grade")

else:
    print("You are failed")

#Example2 : Simple Calculator

num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))

operator=input("\nEnter the operand to perform the operation : ")

if operator == "+" :
         print(f"\nThe sum of {num1} and {num2} is {num1+num2}")

elif operator == "-" :
    print(f"The difference of {num1} and {num2} is {num1-num2}")

elif operator == "*" :
    print(f"The product of {num1} and {num2} is {num1*num2}")

elif operator == "%" :
    print(f"The modulus of {num1} and {num2} is {num1%num2}")

elif operator == "/" :
    print(f"The division of {num1} and {num2} is {num1/num2}")

#<----------------------------------------------------------------------------------------------------------------------------------------------------------------->
#Simple Calculator Version 2:

num1 = int(input("Enter first operand : "))
num2 = int(input("Enter second operand : "))

operator = int(input("Enter your choice \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division\n"))

if operator == 1 :
    print(f"The sum of {num1} and {num2} is {num1+num2}")

elif operator == 2 :
    print(f"The difference of {num1} and {num2} is {num1-num2}")

elif operator == 3 :
    print(f"The product of {num1} and {num2} is {num1*num2}")

elif operator == 4 :
    print(f"The division of {num1} and {num2} is {num1/num2}")

else:
    print("Entered an invalid option")
#<----------------------------------------------------------------------------------------------------------------------------------------------------------------->


#Example 3: Even, Odd Calculator

num = int(input("Enter a number : "))

if num % 2 == 0 :
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")



#Example 4: Positive, Negative, Zero identifier
num = int(input("Enter a number : "))

if num > 0:
    print(f"{num} is positive number")
elif num < 0:
    print(f"{num} is negative number")
else:
    print("Entered number is zero")
'''






