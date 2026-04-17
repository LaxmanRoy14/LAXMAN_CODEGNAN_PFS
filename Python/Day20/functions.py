
functions ()
------------
--> this a block of code whicih is reusuable.
--> Two types
---> 1. Built in Functions
---> 2. User defined functions

1. Built In :
--------------

They comes with the program itself, they are already defined ex- print(),append(),sort()

2. User Defined :
-----------------

they are defined by the user as per his requirements ex-ADD FUNCTION FOR ADDING TWO NUMBERS.

NOTE :
--------

Its starts with def keyword followed by func name and calling func.
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


1. EVEN OR ODD

a = 5
def even_checker(a ):
    if a%2 ==0:
        print(f'{a} is a even num')
    else:
          print(f'{a} is not a even num')
even_checker(a=2)

2. PRIME NUMBER

n = int(input("enter a number: "))
count = 0
def prime_check(Num, a) :
    for j in range(1,Num+1):
        if Num % j == 0:
            a += 1
    if a  == 2:
        print("Prime")
    else:
        print("Not prime")
prime_check(n, count)

3. Palindrome :

n = input("Enter String: ")
empty = ""
def palindrome(n, empty):
    for i in n:
         empty = i+empty
    if empty == n:
         print(f'{n} is a palindrome')
    else:
          print(f'{n} is not a palindrome')
palindrome(n, empty)

4. Fibonacii :

n = int(input("Enter the number: "))
n1=0
n2=1
def fib(n,n1,n2):
    print(n1,n2,end=" ")
    for i in range(n):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3,end=" ")
fib(n,n1,n2)
    

          
             
