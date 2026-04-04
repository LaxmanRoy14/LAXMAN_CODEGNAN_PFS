# Simple Expense Splitter

members = input("Enter names (comma separated): ").split(",")
members = [m.strip().capitalize() for m in members]

expenses = {}

# Initialize expenses
for person in members:
    expenses[person] = 0

n = int(input("Enter number of expenses: "))

# Taking expense inputs
for i in range(n):
    print(f"\nExpense {i+1}")
    
    payer = input("Who paid? ").capitalize()
    amount = float(input("Amount: "))
    
    if payer in expenses:
        expenses[payer] += amount
    else:
        print("Invalid name! Skipping...")

# Calculate total and share
total = sum(expenses.values())
share = total / len(members)

print("\n--- Summary ---")
print("Total Expense:", total)
print("Each should pay:", share)

# Calculate balances
balances = {}
for person in members:
    balances[person] = expenses[person] - share

print("\n--- Balances ---")
for person in balances:
    if balances[person] > 0:
        print(person, "gets back", round(balances[person], 2))
    else:
        print(person, "owes", round(-balances[person], 2))

# Settlement logic (simple)
print("\n--- Settlement ---")

for p1 in balances:
    for p2 in balances:
        if balances[p1] < 0 and balances[p2] > 0:
            amount = min(-balances[p1], balances[p2])
            
            if amount > 0:
                print(p1, "pays", p2, ":", round(amount, 2))
                
                balances[p1] += amount
                balances[p2] -= amount
