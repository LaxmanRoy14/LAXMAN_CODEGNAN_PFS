expenses = []

budget = int(input("Enter your daily budget: "))
n = int(input("Enter number of expenses: "))

for i in range(n):
    print(f"\nExpense {i+1}")
    
    category = input("Enter category (Food/Travel/Shopping/Others): ")
    amount = int(input("Enter amount: "))
    
    expenses.append([category, amount])

# -------- Calculations --------

total_spent = 0
food_total = 0
shopping_total = 0

for e in expenses:
    total_spent += e[1]
    
    if e[0].lower() == "food":
        food_total += e[1]
    elif e[0].lower() == "shopping":
        shopping_total += e[1]

remaining = budget - total_spent

# -------- Conditions --------

# Budget Status
if total_spent > budget:
    status = "Overspending"
elif total_spent == budget:
    status = "Budget Exhausted"
else:
    status = "Within Budget"

# Insights
food_msg = ""
shopping_msg = ""

if total_spent > 0:
    if food_total / total_spent > 0.5:
        food_msg = "High spending on Food"
    
    if shopping_total / total_spent > 0.3:
        shopping_msg = "Control Shopping expenses"

# -------- Output --------

print("\n===== EXPENSE REPORT =====")
print("Total Spent:", total_spent)
print("Budget:", budget)
print("Remaining:", remaining)
print("Status:", status)

print("\nCategory Insights:")
print("Food:", food_total)
print("Shopping:", shopping_total)

if food_msg:
    print(food_msg)

if shopping_msg:
    print(shopping_msg)
