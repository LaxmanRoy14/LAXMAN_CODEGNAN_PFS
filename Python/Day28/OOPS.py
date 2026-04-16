#OPPS
'''
--> Object Oriented Programming System is a style of programming
where we model real world entities as objects that contains both data and functions.
--> It allows us to create classes and objects, which can have their own properties and behaviors.
--> Reusability: OOP allows us to create reusable code by defining classes that can be instantiated multiple times.
--> Scalability: OOP allows us to create complex systems by breaking them down into smaller, more manageable pieces (classes and objects).
--> Maintainability: OOP allows us to create code that is easier to maintain and modify, as we can make changes to a class without affecting the rest of the code.
'''

#Class
'''
--> Class:
A class is a blueprint or template for creating objects.
It defines the properties and behaviors that the objects of that class will have.

--> Syntax:
class class_name:
    def __init__(self):
        pass
'''

#Object
'''
--> Object:
An object is an instance of a class.
It is created from a class and has its own unique identity and state.
--> Syntax:
object_name = class_name()
'''

class Car:
    pass
car1 = Car() #object of class Car
car2 = Car() #object of class Car

#Attributes
'''--> Attributes:
These are variables that hold data associated with an object or class.
--> Syntax:
object_name.attribute_name = value
'''

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")
print(car1.brand) #Output: Toyota

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
animal1 = Animal("Leo", "Lion")
animal2 = Animal("Mia", "Cat")
animal3 = Animal("Max", "Dog")
print(animal1.name, animal1.species) #Output: Leo Lion
print(animal2.name, animal2.species) #Output: Mia Cat
print(animal3.name, animal3.species) #Output: Max Dog