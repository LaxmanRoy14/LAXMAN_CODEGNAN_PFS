#STUDENT_REPORT

name = input("Enter your name : ")
maths = int(input("Enter marks obtained in maths : "))
phy = int(input("Enter marks obtained in physics : "))
chem = int(input("Enter marks obtained in chemistry : "))
attendance = int(input("Enter your attendance (%) : "))
course = input("Enter your course : ")
total = maths + phy + chem
average = total / 3
is_pass = average >= 40
is_distinction = average >= 75
eligible = (attendance >= 75) and (average >= 40)
courses = ["python", "java", "c++"]
course_valid = course in courses

status_map = {
    True: "Yes",
    False: "No"
}

pass_map = {
    True: "Pass",
    False: "Fail"
}

course_map = {
    True: "Valid Course",
    False: "Invalid Course"
}

# Step 9: Output
print("\n------------- STUDENT REPORT ------------")
print(f"Name: {name}")

print(f"Total Marks: {total}")
print(f"Average (with bonus): {average:.2f}")

print(f"Pass Status: {pass_map[is_pass]}")
print(f"Distinction: {status_map[is_distinction]}")

print(f"Attendance: {attendance}%")
print(f"Exam Eligibility: {status_map[eligible]}")

print(f"Course Status: {course_map[course_valid]}")


print("=" * 40)
