#Lambda Function
'''
--> This is also called as anonymous function.
--> A lamda function can take n number of arguments, but only have one expression

Syntax
------------
lambda (keyword) arguments : expression
'''

#Example1
add = lambda num1 , num2 : num1 + num2
print(add(int(input("Enter 1st number : ")),int(input("Enter 2nd number : "))))

#Example2
some = lambda n1, n2, n3 : (n2 - n1)*n3
print(some(4,9,2))


#Example3
speed = lambda d, t : d/t
print(speed(int(input("Enter the distance : ")),int(input("Enter the time : "))))
