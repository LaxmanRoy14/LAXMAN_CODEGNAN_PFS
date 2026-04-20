'''
Constructor (__init__)
-------------------------
--> A constructor is a special method used to initialize object data
'''
#Example:
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
# animal1 = Animal("Leo", "Lion")
# animal2 = Animal("Mia", "Cat")
# animal3 = Animal("Max", "Dog")
# print(animal1.name, animal1.species) #Output: Leo Lion
# print(animal2.name, animal2.species) #Output: Mia Cat
# print(animal3.name, animal3.species) #Output: Max Dog

#Example2
class student:
    def __init__ (self, name, ID):
        self.name = name
        self.ID = ID
    
    def display(self):
        print(self.name, self.ID)

stu_1 = student("Roy", 777)
stu_1.display()