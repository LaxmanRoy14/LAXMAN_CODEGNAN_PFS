# List Methods Demonstration Program

print("----- List Methods Demo -----")

# Initial list
numbers = [3, 1, 2]
print("Original List:", numbers)

# append()
numbers.append(4)
print("After append(4):", numbers)

# extend()
numbers.extend([5, 6])
print("After extend([5,6]):", numbers)

# insert()
numbers.insert(1, 10)
print("After insert(1,10):", numbers)

# remove()
numbers.remove(10)
print("After remove(10):", numbers)

# pop()
numbers.pop(2)
print("After pop(2):", numbers)

# count()
print("Count of 2:", numbers.count(2))

# index()
print("Index of 3:", numbers.index(3))

# sort()
numbers.sort()
print("After sort():", numbers)

# reverse()
numbers.reverse()
print("After reverse():", numbers)

# copy()
new_list = numbers.copy()
print("Copied List:", new_list)

# clear()
numbers.clear()
print("After clear():", numbers)
