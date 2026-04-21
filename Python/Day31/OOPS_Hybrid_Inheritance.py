'''
Hybrid Inheritance
-------------------
--> This is a combination of two or more types of inheritance,
    such as combination of any two of single, multiple, multi-level, hierarchical Inheritances.
'''
#Example
class Person:
    def show_person(self):
        print("I am a person")
class Student(Person):
    def show_student(self):
        print("I am a student")
class Teacher(Person):
    def show_teacher(self):
        print("I am a teacher")
class Assistant(Student, Teacher):
    def show_assistant(self):
        print("I am a teaching assistant")

obj = Assistant()
obj.show_person()
obj.show_student()
obj.show_teacher()
obj.show_assistant()

#Example
class Person:
    def show_name(self):
        print("My name is Roy")
class Student(Person):
    def show_course(self):
        print("I'm Studying CSE")
class SportsPlayer(Person):
    def show_sports(self):
        print("I play Cricket")
class College_Captain(Student, SportsPlayer):
    def show_role(self):
        print("I'm College Captain")
any = College_Captain()
any.show_name()
any.show_course()
any.show_sports()
any.show_role()