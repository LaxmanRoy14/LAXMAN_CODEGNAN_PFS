#SALARY BREAKDOWN CALCULATOR
print("Employee Details")
print("=" * 40)
employee_name = input("Enter employee name : ")
base_salary = float(input("Enter base salary : "))
bonus_percentage = float(input("Enter the bonus percentage : "))
tax_percentage = float(input("Enter the tax deduction percentage : "))
bonus = (bonus_percentage / 100) * base_salary
gross_salary = base_salary + bonus
tax = (tax_percentage / 100) * gross_salary
net_salary = gross_salary - tax
print("=" * 40)

print("=" * 15, "Salary Report", "=" * 15)
print("Employee Name : ", employee_name)
print()
print("Base Salary : ", base_salary)
print("Bonus (%) : ", bonus_percentage)
print("Tax (%) : ", tax_percentage)
print()
print("Bonus Amount : ", bonus)
print("Gross Salary : ", gross_salary)
print("Tax Deduction : ", tax)
print()
print("Net Salary : ", net_salary)
print("=" * 40)
