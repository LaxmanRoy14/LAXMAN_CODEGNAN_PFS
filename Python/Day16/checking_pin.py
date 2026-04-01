#Checking the pin number
icic_roy_ac_details = {"Name" : "Roy",
                       "ATM PIN" : "0007"};
print("Welcome to ICIC bank")
print("Please insert your card")
atm_pin = input("Please enter your pin : ")
if len(atm_pin) == 4:
    if atm_pin == icic_roy_ac_details['ATM PIN']:
        print("The pin is correct")
    else:
        print("You have entered an incorrect pin.")
else:
    print("Please enter a 4 digit pin")
