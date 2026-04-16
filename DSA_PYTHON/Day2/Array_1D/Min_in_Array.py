# n = list(map(int,input().split()))
# print(min(n))
n = list(map(int,input().split()))
minimum = n[0]
for i in n:
    if i < minimum:
        minimum = i
print(minimum)