arr = list(map(int, input().split()))
print(f"Array before reversal: {arr}")
n = len(arr)
for i in range(len(arr)):
    if i > ((n-i) - 1):
        break
    else:
        arr[i], arr[(n-i) - 1] = arr[(n-i) - 1], arr[i]
    
print(f"Array after reversal: {arr}")