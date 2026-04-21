'''
Muliti-Level
-------------
--> This occurs when a class inherits from a child class,
    creating a grandparent --> Parent --> Child in this structure
'''
#Example
class Grandparent:
    def Show_GrandParent(self):
        print("I'm GrandParent")
class Parent(Grandparent):
    def Show_Parent(self):
        print("I'm Parent")
class Child(Parent):
    def Show_Child(self):
        print("I'm Child")

any = Child()
any.Show_GrandParent()
any.Show_Parent()
any.Show_Child()

#Example2
class Employee:
    def get_employee(self):
        print("Employee Name: UMP")
class Manager(Employee):
    def get_manager(self):
        print("He manages the work")
class TeamLead(Manager):
    def get_teamlead(self):
        print("The teamlead will guide the work and assign the work")

h = TeamLead()
h.get_teamlead()
h.get_manager()
h.get_manager()
