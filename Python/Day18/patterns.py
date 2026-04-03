#Patterns
#1 right triangle pattern
'''
input-3
output-
*
**
***
'''
'''
i=1
num = int(input("Enter the number : "))
for i in range(num+1):
    for j in range(i):
        print("*", end = "") # To get stars in single row
    print() # To get new line
'''
#2 Number Triangle-1
'''
input-5
output-
01
012
0123
01234
'''
'''
num = int(input("Enter the number : "))
for i in range(num+1):
    for j in range(i):
        print(j, end = "") # To get stars in single row
    print() # To get new line
'''

#3 Number triangle-2
'''
input-4
output-
1
22
333
4444
'''
'''
num = int(input("Enter the number : "))
for i in range(num+1):
    for j in range(i):
        print(i, end = "") # To get stars in single row
    print() # To get new line
'''
#4 Squares
'''
input - 3
output -
***
***
***
'''
'''
i=1
num = int(input("Enter the number : "))
for i in range(num):
    for j in range(num):
        print("*", end = "") # To get stars in single row
    print() # To get new line
'''
#5 reverse triangle
'''
input-3
output-
***
**
*
'''

'''
num = int(input("Enter the number : "))
for i in range(num):
    for j in range(num - i):
        print("*", end = "")
    print()
'''
#6 Pyramid stars
'''
input-5
output-
    *
   * *
  * * *
 * * * *
* * * * *
'''

'''
num = int(input("Enter a number : "))
for i in range(num):
    print(" "*(num-i), end = "")
    for j in range(i+1):
        print("*", end = " ")
    print()
'''
