'''
print(9+8)
print("Python" + "Programming")
print([1,2] + [3,4]) #Concatenation
'''
#Concatenation
'''
Concatenation
-----------------------
This is nothing but, a + behaviour

case -1
----------
integers --- This will act as addition for the int

case-2
---------
For other datatypes (we have to use same type) this (+) acts as concatination

print("Roy" + [1,2]) #We cannot concatinate two different datatypes
print("A" + 1) #TypeError: can only concatenate str (not "int") to str
print(2.3 + 1) #no error
'''

#Tuple

'''
#Definition
This is a collection of different datatypes and this is represented by "()" and is separates by comma(,)
#Example
Thing = (1,"Teja",[12,4],(6,7))
print(Thing)
'''

#Slicing
'''
Thing = (12, 89, "Python", (23, "Roy", [67, "Python is a language",(7,8)], [8, ("Python",[34, 9])]))
print(Thing)
print(Thing[3][2][1][9])
'''

#Examples

'''
#1. Swapping
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

print(f"Before swapping : \nnum1 = {num1}\nnum2 = {num2}")

num1, num2 = num2, num1

print(f"\nAfter swapping : \nnum1 = {num1}\nnum2 = {num2}")
'''

'''
#2. Leap year

leap_year = int(input("Enter a year : "))
if (leap_year % 4 == 0 and leap_year % 100 != 0) or leap_year % 400 == 0:
    print(f"Yes, {leap_year} is a leap year")
else:
    print(f"No, {leap_year} is a leap year")
'''































