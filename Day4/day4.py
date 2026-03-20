'''
Operators --> An operator is a symbol that performs an operation
on one or more values (operands) and produces a result.

Operators are primarily used for :
-->Calculate Values
-->Compare Values / Inputs
-->Make Decisions
-->Control The Program Flow

There are majorly 7 categories of Operations in Python. They are :
-->1.Arithmetic Operators
-->2.Assignment Operators
-->3.Comparision Operators
-->4.Membership Operators (in, not in)
-->.5Identity Operators (is, is not)
-->6.Bitwise Operators
-->7.Logical Operators (AND, OR, NOT)
'''

#1.ARITHMETIC OPERATORS (Theory)
'''
1.ARITHMETIC OPERATORS
--> Arithmetic operators perform mathematical operations such as

# + --> Addition
# - --> Subtraction
# * --> Multiplication
# / --> Division (Returns the result in float value)

# ** --> Exponent
# % --> Modulus (Returns the Remainder)
# // --> Integer Division 
'''

#1.Arithmetic Operations (Examples)
'''
a = 5
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b) # Returns the result in float values
print(a**b) # Returns the exponential value

print(a % b) # Modulus Division --> Returns the remainder
print(a // b) # Floor / Integer Division --> Returns the Quotient discards
'''

'''
num1=int(input("Enter the first value : "))
num2=float(input("Enter the first value : "))
result = (num1 + num2)*4

# Standard Notation
print("The result is :",result)

# f-string Notation
print(f'The result is : {result}')
print(f'The result of {num1} and {num2} is {result}')
'''

#2.Assignment Operators (Theory)

'''
2.Assignment Operators

# --> "=" Assign
# --> "+=" Addtion Assignment
# --> "-=" Subtraction Assignment
# --> "*="
# --> "/="
# --> "%="
# --> "//="
# --> "**="

#They are majorly used for code repititions in application usage
'''

#2.Assignment Operators (Examples)
'''
a = 4
b = 3

# --> +=
a += 2 # --> a = a+2
print(a) # a=6
b += a
print(b) # b = 9

#In similar way let us check for -=, *=, **=, /=, %=, //=,

# --> -=
b -= 3 # b = b - 3
print(b)

print(f'The ubdated values of "a" and "b" are {a} and {b}')

b *= a
print(b)

b **= a
print(b)

b /= a
print(b)

b %= a
print(b)

b //= a
print(b)
'''

#3.Relational or Comparition Operators (Theory)
'''
#3.Relational or Comparition Operators --> They always return boolean values (True / False)

# --> == is equal to
# --> != not equal to
# --> < less than
# --> > greater than
# --> <= less than equal to
# --> >= greater than equal to
'''

#3.Relational Operations (Examples)
'''
a = int(input("Enter a value : "))
b = int(input("Enter another value : "))

print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
'''

#4.MEMBERSHIP OPERATOR (Theory)
'''
#4.Membership Operators --> They check for the existance of an object in a collection
# --> in
# --> not in
'''

#4.MEMBERSHIP OPERATOR (Example)
'''
a = "laxman"
print(type(a))
print('a' in a)
print('z' in a)
print('z' not in a)

b = [12, 6, 3, 4]
c = int(input("Enter the value to check in the list : "))
print(c)
print(c in b)
print(c not in b)
'''

#5.LOGICAL OPERATORS (Theory)

'''
#5.LOGICAL OPERATORS --> They are used to combine multiple conditions
# --> and
# --> or
# --> not
'''

#5.LOGICAL OPERATORS (Examples)
'''
age = int(input("Enter the age : "))
vote_right = True

print(age >= 18 and vote_right) #both conditions to be True, then only True
print(age > 18 or vote_right) #any one condition is true, then result is true
print(not vote_right)
'''

#6.IDENTITY OPERATORS (Theory)
'''
6. Identity Operators
--> They check the memory location and validate.
we used (id) Function it is different from == operator --> is, is not
'''

#6.IDENTITY OPERATORS (Examples)
'''
a = [1, 2, 4]
b = [1, 2, 4]
 
print(a==b)

print(id(a))
print(id(b))

print(a is b)
print(a is not b)

c = b
 
print(c)
print(id(c))
print(c is b)
'''

#7.BITWISE OPERATORS(Theory)
'''
#Bitwise Operators :
--> Bitwise AND "&"
--> Bitwise OR "|"
#They perform bitwise operations
#We get the result (Remember the binary conversion)
'''

#7.BITWISE OPERATORS(Examples)
'''
print(5 & 3)
print(bin(5)) #Returns binary number
'''
