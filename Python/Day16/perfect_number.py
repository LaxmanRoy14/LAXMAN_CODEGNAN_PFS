#Perfect Number
per_num = int(input("Enter a number : "))
factor_sum = 0
for j in range(1,per_num):
    if per_num % j == 0:
        factor_sum+=j
if factor_sum == per_num:
    print(f"{per_num} is a perfect number")
else:
    print(f"{per_num} is not a perfect number")
