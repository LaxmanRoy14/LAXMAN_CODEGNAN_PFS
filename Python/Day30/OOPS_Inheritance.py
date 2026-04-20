#Inheritance
#------------
'''
--> This allows a child class(subclass) to acquire the attributes and methods
    of a parent class(Base class) this is called Inheritance

Types of Inheritance
---------------------
1. Single Inheritance
2. Multiple Inheritance
'''
#Super()
#------------
'''
--> This is used to call methods of the parent class from the child class
'''
#Example
class parent:
    def display(self):
        print("This is parent method")
class child(parent):
    def display(self):
        super().display()
        print("This is child method")

any = child()
any.display()

#1. Single Inheritance
'''
One parent --> One child
'''
#Example
class parent:
    def display(self):
        print("This is parent method")
class child(parent):
    def display(self):
        super().display()
        print("This is child method")

#2. Multiple Inheritance
'''
One child can have multiple parents
'''
#Example
class father:
    def skill_1(self):
        print("Father: Hard Working")
class mother:
    def skill_2(self):
        print("Mother: Cooking")
class child(father, mother):
    def skill_3(self):
        print("Child: Coding")
skill = child()
skill.skill_1()
skill.skill_2()
skill.skill_3()

#3. MultiLevel Inheritance