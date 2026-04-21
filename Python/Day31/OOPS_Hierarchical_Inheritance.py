'''
Heirarchical Inheritance
-------------------------
'''
class Parent:
    def parent_(self):
        print("I'm Parent")
class Child_1(Parent):
    def child_(self):
        print("I'm 1st child")
class Child_2(Parent):
    def _child(self):
        print("I'm 2nd child")
class Child_3(Child_1, Child_2):
    def child(self):
        print("I'm the child")
thing = Child_3()
thing.parent_()
thing.child_()
thing._child()
thing.child()
