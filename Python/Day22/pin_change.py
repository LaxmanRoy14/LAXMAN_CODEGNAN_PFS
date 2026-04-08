#Checking the PIN number, Withdrawing the amount, showing the balance,Deposit the amount, Changing the PIN
icic_roy_ac_details = {"Name" : "Roy",
                       "ATM PIN" : "0007",
                       "Balance" : 5000};
print("Welcome to ICIC bank")
print("Please insert your card")
atm_pin = input("Please enter your pin : ")
if len(atm_pin) == 4:
    if atm_pin == icic_roy_ac_details['ATM PIN']:
        print("The pin is correct")
        user_choice = int(input("Enter the option number :\n1. Withdraw\n2. Deposit\n3. PIN change\n"))
        if user_choice == 1:
            money_w = int(input("Enter money you want to withdraw: "))
            if money_w <= icic_roy_ac_details['Balance']:
                icic_roy_ac_details['Balance'] -= money_w
                print(f"Remaining balance is {icic_roy_ac_details['Balance']}")
            else:
                print("Insufficient balance")
        elif user_choice == 2:
            deposit_m = int(input("Please enter the amount you want to deposit : "))
            if deposit_m % 100 == 0 and deposit_m >= 5000:
                icic_roy_ac_details['Balance'] += deposit_m
                print(f"You have deposited Rs{deposit_m}\nNow your current balance is Rs{icic_roy_ac_details['Balance']}")
            else:
                print(f"{deposit_m} you have entered is not round figure or less than 5000/-")
        elif user_choice == 3:
            old_pin = input("Enter your old pin : ")
            if old_pin == icic_roy_ac_details['ATM PIN']:
                new_pin = input("Enter new PIN number : ")
                if len(new_pin) == 4:
                    if new_pin != icic_roy_ac_details['ATM PIN']:
                        icic_roy_ac_details['ATM PIN'] = new_pin
                        print(f"PIN changed successfully.\nNew PIN is {new_pin} ")
                    else:
                        print("New pin shouldn't be same as old pin")
                else:
                    print("PIN entered is not 4 digits. Please enter 4 digit PIN")
            else:
                print("You entered the wrong pin")
    else:
        print("You have entered an incorrect pin.")
else:
    print("Please enter a 4 digit pin")
