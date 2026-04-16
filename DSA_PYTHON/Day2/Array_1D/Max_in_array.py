# n = list(map(int,input().split()))
# print(max(n))
n = list(map(int,input().split()))
maximum = n[0]
for i in n:
    if i > maximum:
        maximum = i
print(maximum)