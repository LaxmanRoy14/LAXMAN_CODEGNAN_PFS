lst = [7,18,45,77,10,9,33,100]

#Method-1
even=[]
odd=[]
for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"Sum of even numbers is : {sum(even)}")
print(f"Sum of odd numbers is : {sum(odd)}")

#Method-2
sum_even=0
sum_odd=0
for i in lst:
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print(f"Sum of even numbers is : {sum_even}")
print(f"Sum of odd numbers is : {sum_odd}")
