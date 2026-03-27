#Strings
'''
Strings --> String is a collection of characters, which represented inside (" ") or (' ')
and we can access the string characters using indexing and slicing.
This is also immutable where we cannot modify on that particular variable.
'''
any = 'Python Programming' #string

#Indexing
'''
print(any[7]) #Indexing
print(any[7,8,9]) #Type Error : String indices must be integers, not tuples
print(any[-6]) #Negative indexing is also possible.
print(any[30]) #Gives error as index is out of range
'''
#Slicing
'''
print(any[7 : 13])
print(any[:6]) #By default the starting index will be zero
'''

#Strings are immutable
'''
print(any.replace("Python","Java"))

-->Strings are immutable where we cannot modify on that particular variable.
so = any.replace("Python","Java")
print(any)
print(so)
'''

#Task1
'''
a_day = "I'm Laxman from Vizag, I'm a fresher as full stack developer"
print(f"My name is {a_day[4:10]}")
print(f"I'm from {a_day[16:21]}")
print(f"I'm a {a_day[-21:]}")
'''

#Task2 (reversing a string)
'''
name="Laxman"
print(f"Reversed string {name[::-1]}")
'''

#Task3 (length of string)
'''
-->len() method is used to find the char present in the string or find the length of the string

a_day = "I'm Laxman from Vizag, I'm a fresher as full stack developer"
digit=12
print(len(a_day))
#print(len(digit)) #Object Type 'int' as no method len()
'''

#-->Note : We can convert a string into integer, if the string contain integer values.
'''
some = "123"
num = int(some)
print(type(num))

s = "123p"
#n= int(s) #gets error as the string 's' does'nt contain all integer values
'''

#Methods of string(Inbuilt)

#1. split()
'''
--> removes whatever sub-string is given in the string, and the output is in the list[].
-->It will give the separated things in each index.
-->It is used to split words in a sentence.
syntax--> variable_name.split("substring")

#Example
some = "Python is a programming language"
print(some.split()) #By default, it removes the spaces
print(some.split(" "))
print(some.split("programming"))
'''

#2. lower()
'''
-->This is used to convert all letters in the string to lowercase
syntax---> variable_name.lower()

#Example
some = "PyThon iS a PrograMming lanGuage"
print(some.lower())
'''

#3. upper()
'''
-->This is used to convert all letters in the string to uppercase
syntax---> variable_name.upper()

#Example
some = "Python is a programming language"
print(some.upper())
'''

#4. replace()
'''
--->This is used to replace old str with the new str
syntax---> Variable_name.replace("old string","new string")

#Example
some = "Python is a programming language"
print(some.replace("programming","nrml"))
'''

#Task3 (Check if a substring is present or not)
'''
some = "Python is a programming language"
if "Python" in some:
    print("Yes")
else:
    print("No")
'''
















