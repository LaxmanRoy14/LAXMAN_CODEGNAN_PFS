'''
a = 9
for j in range(1,10): #here j in the temporary variable and we dont get error while using it 
    print(j)
<------------------------------------------------------------------------------------------------------------------->
Range() -----> This is used to generate number
Synatx ----> range(start,end,step)
-------
for j in range(0,21,2):
    print(j)
<------------------------------------------------------------------------------------------------------------------->
any = "123"
print(int(any))#string to int when there are only integers in the string.
print(list(any)) #string to list.
print(tuple(any)) #string to tuple.

so = 123
print(str(so)) #int to string
print(float(so)) #int to float

an = [1,2,3]
print(str(an)) #list to string
print(tuple(an)) #list to tuple

so = (2,3,5,6)
print(list(so))

a = [(1,2),(3,4)]
print(dict(a))

a = "laxman"
empty_ = " "
for j in a:
    empty_ = j + empty_ #empty_ += j
    print(empty_)
print(a[::-1])

a = "madam"
empty_ = ""
for j in a:
    empty_ = j + empty_  #empty_ += j
if empty_ == a:
    print("Palindrome")
else:
    print("Not a Palindrome")
'''
for num in range (1,100):
    if num % 2 == 0:
        print(f"{num} is a Even Number")
    else:
        print(f"{num} is a Odd Number")
