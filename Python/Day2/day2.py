'''

Variables --> Variables are basically a named storage location that is used to hold the
data in the memory, to make it simple it is the lable which points out to a value --> Storage placeholders

Rules for defining Variables:
-->Variable can contain A-Z, a-z, 0-9
-->Variable starts with uppercase, lowercase letters, even with a underscore(_)
-->Variable cannot start with symbols (@, #, $...) and numbers(0-9)

Better preferable way is to go with general purpose.
Example --> If you want to store your details,
then you can name variables as name, email_id, account_id and so on.



m = 1
n = 5
m = 25

#Python is dynamically typed, you need not define the datatypes and also
#Only the recent value to the variable with same name is pointed.

print(m)
print(n)

#Some common syntax errors are:

#1a23 = 25 #Syntax Error

#@werf = 4.5 #Syntax Error

#$dsf = 25 #Syntax Error

#We can store personal details as:

name = "Laxman Roy"
location = "Visakhapatnam"
age = 21
emailid = "laxmanroy85002@gmail.com"
email_id = "laxmanroy85002@gmail.com"
print(name, location, age, email_id)

#How to assign multiple values to a variables

akash, praneeth, ajay = 21, 20, 23
print(akash)
print(praneeth)
print(ajay)

#Assigning same values to multiple variables
x = y = z = 21
print(x , y, z)

#KEYWORDS

#Keywords are reserved woords, which will have specific usage
#There are 35 keywords in python

#Never use keywords as identifiers.
#Example -->
#if =23
#lambda = 'saketh'
#False = 0 #cannot assign

#Python is case sensitive
false = 25

#Identifiers are names given to variables, functions, classes, objects...

#Literals are fixed values to a Identifier
name = 'saketh'

#name is identifier, saketh is literal

#COMMENTS
#Single line comments --> we use '#'
#Multi line comments -->(Start and end with triple quotes)

#DATATYPES

#Built-in Datatypes -->Numeric, Boolean, Collections

#Numeric datatypes --> int, float, complex

#int --> Used as count, values, quantities
#float --> Used for temparatures, percentages, price and so on
#complex --> Used for specific conversions (real and imaginary)

#Example for int
count = 40
print(count)
print(type(count))

#Example for float
price = 175.25
print(price)
print(type(price))

#Example for complex
value = 2+3j
print(value)
print(type(value))

#If we give 'j3' it considers 'j3' as another variable, but not imaginary
j3 = 25
val = 2 + j3
print(value)
print(type(val))

#TYPECASTING

#--> Converting one datatype to another datatype

#int --> float, complex

age = 25
print(type(age))

b = float(age)
print(b)
print(type(b))

c = complex(age)
print(c)
print(type(c))

#float --> int, complex

weight=60.5
print(type(weight))

d = int(weight)
print(d)
print(type(d))

e = complex(weight)
print(e)
print(type(e))

#complex --> int, float

f = 2+5j
print(f)
print(type(f))

#g = int(f) #Complex to int is not possible

#h = float(f) #Complex to float is not possible

#BOOLEAN DATATYPE
#--> Validation --> TRUE / FALSE

a = True
print(a)
print(type(a))

#Typeconversion of bool

b = int(a)
print(b)
c = float(a)
print(c)
v=complex(float(int(False)))
print(v)
print(type(v))


#INPUT and OUTPUT

#Input --> input()
#Output --> print()

l = 5
print(l)

l = input("Enter a value : ") #Any input will be stored as 'String'
print(l)
print(type(l))

l = int(input("Enter a value : "))
print(l)
print(type(l))

b = float(input("Enter a value : "))
print(b)
print(type(b))
'''
#Now let's work on a simple case study using above concepts

#FEE CALCULATOR

#Details of the Student
print("Enter the details of Student")
print("---------------------------------\n")
name = input("Enter the student name : ")
print("\nENTER THE FEE DETAILS")
admission_fees = int(input("Enter the Admission Fees : "))
tuition_fees = float(input("Enter the Tuition Fees : "))
hostel_fees = float(input("Enter the Hostel Fees : "))

#Calculate the Total Fees
total_fees = admission_fees + tuition_fees + hostel_fees

#Student Details
print("----------------------------------")
print("\nSTUDENT DETAILS")
print("----------------------------------")
print("Student name is : ", name)
print("Admission Fees is : ", admission_fees)
print("Tuition Fees is : ", tuition_fees)
print("Hostel Fees is : ", hostel_fees)
print("Total Fees is : ", total_fees)
print("------------------------------------")
