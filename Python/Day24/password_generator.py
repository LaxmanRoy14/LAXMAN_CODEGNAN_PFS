password = input("Enter your password: ")

score = 0

# Length check
if len(password) >= 8:
    score += 1

# Uppercase check
for ch in password:
    if ch.isupper():
        score += 1
        break

# Lowercase check
for ch in password:
    if ch.islower():
        score += 1
        break

# Digit check
for ch in password:
    if ch.isdigit():
        score += 1
        break

# Special character check
special = "!@#$%^&*"
for ch in password:
    if ch in special:
        score += 1
        break

# Result
if score >= 4:
    print("Strong Password 💪")
elif score >= 2:
    print("Medium Password ⚡")
else:
    print("Weak Password ⚠️")
