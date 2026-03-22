# Simple Login System

# Predefined credentials
stored_username = "laxman"
stored_password = "1234"

# Maximum attempts
max_attempts = 3

# Attempt counter
attempts = 0

print("=== Welcome to Secure Login System ===")

# Loop for login attempts
while attempts < max_attempts:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Check credentials
    if username == stored_username and password == stored_password:
        print("\n✅ Login Successful! Welcome,", username)
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"\n❌ Invalid credentials. Attempts left: {remaining}")

# If all attempts are used
if attempts == max_attempts:
    print("\n🔒 Account Locked due to too many failed attempts.")
