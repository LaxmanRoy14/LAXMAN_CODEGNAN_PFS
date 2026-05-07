#Checking the PIN number, Withdrawing the amount, showing the balance,Deposit the amount, Changing the PIN
icic_roy_ac_details = {"Name" : "Roy",
                       "ATM PIN" : "0007",
                       "Balance" : 5000,
                       "History" : []};
print("Welcome to ICIC bank")
print("Please insert your card")
atm_pin = input("Please enter your pin : ")
if len(atm_pin) == 4:
    if atm_pin == icic_roy_ac_details['ATM PIN']:
        print("The pin is correct")
        while True:
            print("\n1. Withdraw")
            print("2. Deposit")
            print("3. Pin Change")
            print("4. Balance")
            print("5. Transaction History")
            print("6. Exit")
            user_choice = int(input("Enter the option number : "))
            
            if user_choice == 1:
                money_w = int(input("Enter money you want to withdraw: "))
                if money_w <= icic_roy_ac_details['Balance']:
                    icic_roy_ac_details['Balance'] -= money_w
                    icic_roy_ac_details['History'].append(f"Withdraw amount : {money_w}")
                    print(f"Remaining balance is {icic_roy_ac_details['Balance']}")
                else:
                    print("Insufficient balance")
            
            elif user_choice == 2:
                deposit_m = int(input("Please enter the amount you want to deposit : "))
                if deposit_m % 100 == 0 and deposit_m >= 5000:
                    icic_roy_ac_details['Balance'] += deposit_m
                    icic_roy_ac_details['History'] .append(f"Deposit : {deposit_m}")
                    print(f"You have deposited Rs{deposit_m}\nNow your current balance is Rs{icic_roy_ac_details['Balance']}")
                else:
                    print(f"{deposit_m} you have entered is not round figure or less than 5000/-")
            
            elif user_choice == 3:
                attempts_remaining = 3
                while attempts_remaining > 0:
                    old_pin = input("Enter your old pin : ")
                    if old_pin == icic_roy_ac_details['ATM PIN']:
                        new_pin = input("Enter new PIN number : ")
                        if len(new_pin) == 4:
                            if new_pin != icic_roy_ac_details['ATM PIN']:
                                icic_roy_ac_details['ATM PIN'] = new_pin
                                print(f"PIN changed successfully.\nNew PIN is {new_pin} ")
                                icic_roy_ac_details['History'].append("PIN Changed")
                            else:
                                print("New pin shouldn't be same as old pin")
                        else:
                            print("PIN entered is not 4 digits. Please enter 4 digit PIN")
                    else:
                        attempts_remaining-=1
                        print(f"You entered the wrong pin. You have {attempts_remaining} attempts remaining")
            
            elif user_choice == 4:
                print(f"The current Balance is {icic_roy_ac_details['Balance']}")

            elif user_choice == 5:
                print(f"The transaction History is :\n{icic_roy_ac_details['History']}")

            elif user_choice == 6:
                print("Thank you for using ATM")
                break

            else:
                print("You have entered an incorrect option")
    else:
        print("You have entered an incorrect pin.")
else:
    print("Please enter a 4 digit pin")
