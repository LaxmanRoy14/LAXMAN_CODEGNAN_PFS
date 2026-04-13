#Generators
'''
Generators
---------------
--> This is a special type of function that return an ITERATOR one at a time

Yield
--------
--> It will take a pause and again resume,
      this is not a normal keyword which cannot be used in a normal function.
--> This is used to produce a value and pause execution.

Next()
---------
--> This is used to get next value from a generator
--> When the value is finished, it will stop the iterator
'''

#Example1

def my_generator():
    yield 1
    yield 2
    yield 3
an = my_generator()
print(next(an))
print(next(an))
print(next(an))


#Example2

def square_gen(n):
    for i in range(n):
        yield i*i
for val in square_gen(5):
    print(val)
















