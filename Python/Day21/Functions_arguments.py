#Ways to pass the arguments in a function

#1 Required Arguments
'''
It should match the exact number of parameters in the calling function and the definition function.
'''
'''
num = 9
num_2 = 10
def add(num, num_2):
    print(num+num_2)
add(num, num_2)
'''

#2 Default Arguments
'''
Default argument allows you to define parameters in a user-built function
that take a predefined value if no argument is provided during the function call.
'''
'''
my_name = "Roy"
def add(my_name):
    print(my_name)
add (my_name = "Laxman")
add (my_name = "Prasad")
'''

'''
#Prime Number
def prime_num(num):
    count=0
    for i in range(1,num+1):
        if num % i == 0:
            count+=1
            if count > 2:
                break
    if count  == 2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
num = int(input("Enter a number : "))
prime_num(num)
'''

'''
def any(num, num_3, num_2):
    print(f"num = {num}, num_2 = {num_2}, num_3 = {num_3}")
any(num_2 =7, num = 0, num_3 = 90)
'''

#Own Example for Default Arguments
def sum (num_1=8,num_2=9):
    print(num_1+num_2)
sum(7)
sum(2,3)

#Variable length Arguments
'''
Adding a star (*) before the parameter name in the function 
'''
def name(*candidates):
    print(candidates[2])
name("laxman", "Roy","Teja")


