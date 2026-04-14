#Modules
'''
--> A module is a file in python, is simply a file that contain python code (Functions, Variables, Classes)
--> To use modules we have to use a keyword called import before the module

                                                                                    Types of Modules
                                                                                    ------------------------
                                                              1. Built-in or Inbuilt              2. User-define modules
'''
#Userdefined modules
'''
--> This is developed by the user or programmer inside a file of python code
      and used by called import with filename.
      
#syntax--> import(keyword) file_name
                  file_name.functionality
'''

#Example-1
import my_module
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print(my_module.add(num1, num2))

#Example-2
import prime_check
num = int(input("Enter a num to check for prime : "))
if prime_check.prime_num(num) is True:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

#Built-in or Inbuilt
'''
-->Already these comes with installation and they are ready to use in the program
--> This is developed by the developer
syntax --> import(keyword) module_name
                module_name.functionality
'''
#Example1
import math
print(f"The value of 2 to the power 3 is {math.pow(2,3)}")
print(f"The square root of 25 is {math.sqrt(25)}")
