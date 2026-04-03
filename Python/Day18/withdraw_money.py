#Checking the pin number, Withdrawing the amount, showing the balance
icic_roy_ac_details = {"Name" : "Roy",
                       "ATM PIN" : "0007",
                       "Balance" : 5000};
print("Welcome to ICIC bank")
print("Please insert your card")
atm_pin = input("Please enter your pin : ")
if len(atm_pin) == 4:
    if atm_pin == icic_roy_ac_details['ATM PIN']:
        print("The pin is correct")
        user_choice = int(input("Enter \n1. Withdraw : "))
        if user_choice == 1:
            money_w = int(input("Enter money you want to withdraw: "))
            if money_w <= icic_roy_ac_details['Balance']:
                icic_roy_ac_details['Balance'] -= money_w
                print(f"Remaining balance is {icic_roy_ac_details['Balance']}")
            else:
                print("Insufficient balance")
    else:
        print("You have entered an incorrect pin.")
else:
    print("Please enter a 4 digit pin")
