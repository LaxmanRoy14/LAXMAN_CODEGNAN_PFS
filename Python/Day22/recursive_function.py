#Recursive Functions
'''
Recursion is a programming tehnique where a function calls itself either directly or indirectly to solve a problem
by breaking it into smaller, simpler subproblems.
Recursion is especially used for problems that can be divided into identical smaller tasks, such as mathematical
calculations,tree traversals or divide-and-conquer algorithms.
'''

#Example1
'''
def fibbonaci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibbonaci(num-1) + fibbonaci(num-2)
print()
'''
#example
'''
self.user_info = {"Name" : "Roy",
                       "ATM PIN" : "0007"};
print("Welcome to ICIC bank")
print("Please insert your card")
def validate_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("enter 4 digit pin: ")
        if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
            print("Welcome to ATM")
            return True
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts > 0:
                print(f"Invalid Pin. Attempts left: {self.remaining_attempts}")
            else:
                print("Card blocked. Please contact customer care")
                return False
'''

#Vowels and consonents in a sentence


def Vowel_con(any):
    count_v = 0
    count_c = 0
    count_s = 0
    for i in any:
        if i in "AEIOUaeiou":
            count_v +=1
        elif i == " ":
            count_s +=1
        else:
            count_c +=1
    print(f"Count of vowels is {count_v}\ncount of consonents is {count_c}\ncount of spaces is {count_s}")
any = input("Enter a sentence : ")
Vowel_con(any)





















