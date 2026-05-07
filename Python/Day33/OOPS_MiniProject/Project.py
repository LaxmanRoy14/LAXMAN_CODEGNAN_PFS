class Person:
    def __init__(self, Name, Edu):
        self.Name = Name
        self.Edu = Edu


class Student(Person):
    def __init__(self, Name, Edu, STU_ID, Course):
        super().__init__(Name, Edu,)
        self.Course = Course
        self.STU_ID = STU_ID

    def display(self):
        print("\nStudent Details:\n")
        print("Name:", self.Name)
        print("Education:", self.Edu)
        print("Student ID:", self.STU_ID)
        print("Course:", self.Course)


class Professor(Person):
    def __init__(self, Name, Edu, PROF_ID, Course):
        super().__init__(Name, Edu)
        self.Course = Course
        self.PROF_ID = PROF_ID

    def display(self):
        print("\nProfessor Details:")
        print("Name:", self.Name)
        print("Education:", self.Edu)
        print("Professor ID:", self.PROF_ID)
        print("Courses Teached:", self.Course)

class NonTechnicalStaff(Person):
    def __init__(self, Name, Edu, STAFF_ID, Department):
        super().__init__(Name, Edu)
        self.STAFF_ID = STAFF_ID
        self.Department = Department

    def display(self):
        print("\nNon-Technical Staff Details:")
        print("Name:", self.Name)
        print("Education:", self.Edu)
        print("Staff ID:", self.STAFF_ID)
        print("Department:", self.Department)

stu1 = Student("Laxman", "BTech", "S101", "Python")
stu2 = Student("Roy","BTech", "S102", "Java")
prof1 = Professor("Teja", "M.Tech", "P101", "Python")
staff1 = NonTechnicalStaff("Ravi", "MBA", "N101", "Accounts")

stu1.display()
stu2.display()
prof1.display()
staff1.display()