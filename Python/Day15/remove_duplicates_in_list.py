#To remove duplicates in a list
'''
any = [2,356,8,6,3,2,8]
empty = []
for j in any:
    if j not in empty:
        empty.append(j)
print(empty)
'''

#To remove duplicates in a list With using in-built functions
'''
lst = [1, 2, 2, 3, 4, 3, 5]

for item in lst:   # iterate over a copy
    if lst.count(item) > 1:
        lst.remove(item)

print(lst)
'''
#To remove duplicates in a list without using in-built functions
'''
lst = [1, 2, 2, 3, 4, 3, 5]

i = 0
while i < len(lst):
    j = i + 1
    while j < len(lst):
        if lst[i] == lst[j]:
            lst.pop(j)   # remove duplicate
        else:
            j += 1
    i += 1

print(lst)
'''
