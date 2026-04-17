i = 0
j = 0
a = list(map(int,input().split()))
k = int(input())
n = len(a)
while i < n:
    if a[i] == k:
        print("Element found")
        j =1
        break
    i+=1
if j == 0:
    print("Element not found")