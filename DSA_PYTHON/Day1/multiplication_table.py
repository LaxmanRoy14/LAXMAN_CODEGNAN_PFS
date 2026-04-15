num = int(input("Enter a number: "))
range_table = int(input("Enter the range for multiplication table: "))
for i in range(1, range_table + 1):
    print(num, "x", i, "=", num * i)