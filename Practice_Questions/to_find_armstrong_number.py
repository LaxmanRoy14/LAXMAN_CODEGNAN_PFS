
#To find Amstrong number
so = int(input("Enter a number : "))
length = len(str(so))
amstr = 0
for j in str(so):
    amstr += int(j) ** length
if amstr == so:
    print(f"{so} is Armstrong number")
else:
    print(f"{so} is not aArmstrong number")
