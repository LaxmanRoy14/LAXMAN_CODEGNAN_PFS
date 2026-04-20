#Encapsulation
#---------------
'''
--> The principle of building data(Attributes) and methods that operate on
    the data into a single unit, which is a class
'''

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(15000)
acc.deposit(int(input("Enter deposit amount: ")))
print(acc.get_balance())
