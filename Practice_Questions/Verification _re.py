import re

# Function to validate name
def validate_name(name):
    pattern = r'^\S+$'
    return re.match(pattern, name)

# Function to validate email
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Function to validate phone number
def validate_phone(phone):
    pattern = r'^\d{10}$'
    return re.match(pattern, phone)

# Function to validate password
def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
    return re.match(pattern, password)

# Main function
def main():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    password = input("Enter Password: ")

    if not validate_name(name):
        print("Invalid Name (should not contain spaces)")

    elif not validate_email(email):
        print("Invalid Email")

    elif not validate_phone(phone):
        print("Invalid Phone Number (must be 10 digits)")

    elif not validate_password(password):
        print("Invalid Password")
        print("Password must contain:")
        print("- At least 1 uppercase letter")
        print("- At least 1 number")
        print("- At least 1 special character")

    else:
        print("All inputs are valid")

# Run program
main()