n = list(map(int, input().split()))

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[j] < n[i]:
            n[j], n[i] = n[i], n[j]

print(n)