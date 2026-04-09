#List Comprehension
'''
--> This offers the shorter syntax when you want to create a new list from the existing list

Syntax
----------
variable_name = [expression loop and condition]
'''
old_list = [1,2,3,4,5]
even_list = [j for j in old_list if j%2==0]
odd_list = [j for j in old_list if j%2!=0]
print(even_list,odd_list)
