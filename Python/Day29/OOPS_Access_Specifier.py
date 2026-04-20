#Access Specifiers
'''
Access Specifiers
-------------------
1. Public
2. Protected
3. Private

--> 1. Public
------------------
We can use it anywhere in the program
--> Syntax: name

--> 2. Protected
-------------------
This is only for internal use
--> Syntax: _name

--> 3.Private
------------------
This one is restricted
--> Syntax: __name
'''
#Example
class some:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

obj = some()
print(obj.public)
print(obj._protected)
print(obj._some__private)