# Taking input from user
sentence = input("Enter a sentence: ")

# Initialize counters
vowels = 0
consonants = 0

# Define vowels
vowel_set = "aeiouAEIOU"

# Loop through each character
for char in sentence:
    if char.isalpha():  # Check if it's a letter
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 1

# Output result
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
