# Smart Billing System

print("------ SMART BILLING SYSTEM ------")

# Inputs
name = input("Enter customer name: ")
bill = float(input("Enter total bill amount: "))

member_input = input("Are you a member? (yes/no): ").strip().lower()
festival_input = input("Is there a festival offer? (yes/no): ").strip().lower()

# Convert to boolean
is_member = member_input in ["yes", "y"]
is_festival = festival_input in ["yes", "y"]

# Validation
if bill < 0:
    print("Invalid bill amount!")
else:

    # -------------------------------
    # Percentage Discount (10% + 5% if member)
    # -------------------------------
    percentage_discount = 0

    if bill >= 1000:
        percentage_discount = 0.10 * bill

        if is_member:
            percentage_discount += 0.05 * bill

    # -------------------------------
    # Festival Discount
    # -------------------------------
    festival_discount = 200 if is_festival else 0

    # -------------------------------
    # Loyalty Discount
    # -------------------------------
    loyalty_discount = 500 if bill > 3000 else 0

    # -------------------------------
    # Find Best Discount
    # -------------------------------
    best_discount = max(percentage_discount, festival_discount, loyalty_discount)

    # Identify which discount applied
    if best_discount == percentage_discount:
        discount_type = "Percentage Discount (including membership if applicable)"
    elif best_discount == festival_discount:
        discount_type = "Festival Discount"
    else:
        discount_type = "Loyalty Discount"

    # Final Amount
    final_amount = bill - best_discount

    # -------------------------------
    # Output
    # -------------------------------
    print("\n------ BILL SUMMARY ------")
    print("Customer Name:", name)
    print("Original Amount: ₹", bill)
    print("Discount Applied: ₹", best_discount)
    print("Discount Type:", discount_type)
    print("Final Amount: ₹", final_amount)
    print("--------------------------")
