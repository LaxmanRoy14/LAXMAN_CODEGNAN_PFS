import random
num = random.randint(1,10)
attempts = 5
while attempts > 0:
    user_num = int(input("Guess the number between 1 to 10 : "))
    if user_num == num:
        print("\nCongrants! You guessed it right")
        break
    else:
        attempts -= 1
        print(f"\nWrong Guess! Try again. Attempts remaining {attempts}\n")
        if attempts > 0:
            if user_num > num:
                print("Hint : Guessed Number is more than Actual Number\n")
            else:
                print("Hint : Guessed Number is less than Actual Number\n")
if attempts <= 0:
    print(f"The number is {num}")
        
