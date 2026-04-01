#Counting upper and lower cases in a string
'''
an = input("Enter a sentence : ")
count_u = 0
count_l = 0
count_s = 0
for ch in an:
    if ch.isupper():
        count_u +=1
    elif ch.islower():
        count_l +=1
    else:
        count_s +=1
print(f"There are total {count_u} captial letters,\nThere are total {count_l} small letters,\nThere are total {count_s} spaces.")
'''
#Printing the upper and lower cases separately
an = input("Enter a sentence : ")
capital = []
small = []
for ch in an:
    if ch.isupper():
        capital.append(ch)
    elif ch.islower():
        small.append(ch)
print(f"The capital letters in the sentence are : {capital}")
print(f"The small letters in the sentence are : {small}")
