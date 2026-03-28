#Dictionary
'''
We can store data as "key : value" pair
Keys are unique and we can only give immutable datatypes in the keys
Values --- We can use all datatypes (immutable and mutable)
'''
#Examples
#1
'''
sbi_roy = {"name" : "Teja",
           "name": "Roy"}
print(sbi_roy)
'''
#2
'''
sbi_roy = {"name" : "Teja",
           "Role": "Manager",
           "Salary" : 30000}
print(sbi_roy)
'''
#3
'''
sbi_roy = {"name" : "Teja",
           "Name": "Roy",
           [1,2] : 3}
print(sbi_roy)
#We will get error as
    sbi_roy = {"name" : "Teja",
TypeError: unhashable type: 'list'
'''


#Methods in dictionaries
#----------------------------------------------------------------------
sbi_roy = {"name" : "Teja",
           "Role": "Manager",
           "Salary" : 30000}

#1 keys()--- This method is used to get all keys from the dict
#example
print(sbi_roy.keys())

#2 values()--- This method is used to get all values from the dict
#example
print(sbi_roy.keys())

#3 clear() --- This method is used to clear the data in the dict
#example
sbi_roy.clear()
print(sbi_roy)


#Sets
'''
set{} ---> set data type is a unordered collection and it never allows duplicates
'''
#Example
'''
any = {1, 2, 3, 4, 3}
print(any)
'''


#Methods in dictionary
#------------------------------------------------------
any = {1, 2, 3, 4}
so = {4, 5, 6}
#------------------------------------------------------

#1 union() --- This method is used to add or get 2 different sets without duplicated
#Example
print(any.union(so))

#2 intersection() -- This method is used to find out the common elements from 2 sets
#Example
print(any.intersection(so))

#3 difference() --- This method is used to find the difference from 1st set to the 2nd
#Example
print(any.difference(so))

#4 remove and pop
#remove() --- remvoes the given element
any.remove(1)
print(any)
any.pop()
print(any)



#Task1
user_info = {"name" : "Laxman",
             "account_number" : 123,
             "balance" : 50000,
             "pin" : "3050",
             "account_type" : "savings"}

user_pin = input("Enter your pin number : ")

if user_pin in user_info["pin"]:
    print("Pin is correct")
else:
    print("Pin is incorrect")





























