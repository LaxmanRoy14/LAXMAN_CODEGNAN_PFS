# Original string with mixed content
my_string = "Hello Python 123"
print("Original String:", my_string)

# 1. upper()
print("\nUpper:", my_string.upper())

# 2. lower()
print("Lower:", my_string.lower())

# 3. title()
print("Title:", my_string.title())

# 4. capitalize()
print("Capitalize:", my_string.capitalize())

# 5. swapcase()
print("Swapcase:", my_string.swapcase())

# 6. find()
print("Find 'Python':", my_string.find("Python"))

# 7. index()
print("Index 'Hello':", my_string.index("Hello"))

# 8. replace()
print("Replace:", my_string.replace("Python", "Java"))

# 9. split()
print("Split:", my_string.split())

# 10. join()
words = ["I", "love", "Python"]
print("Join:", " ".join(words))

# 11. startswith()
print("Starts with 'Hello':", my_string.startswith("Hello"))

# 12. endswith()
print("Ends with '123':", my_string.endswith("123"))

# 13. count()
print("Count of 'o':", my_string.count("o"))

# 14. strip()
str_with_spaces = "  hi  "
print("Strip:", str_with_spaces.strip())

# 15. lstrip()
print("Lstrip:", str_with_spaces.lstrip())

# 16. rstrip()
print("Rstrip:", str_with_spaces.rstrip())

# 17. isalpha()
print("Isalpha:", "Hello".isalpha())

# 18. isdigit()
print("Isdigit:", "123".isdigit())

# 19. isalnum()
print("Isalnum:", "Hello123".isalnum())

# 20. isspace()
print("Isspace:", "   ".isspace())
