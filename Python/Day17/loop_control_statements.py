#Continue
'''
continue --- this is used to skip that particular loop
'''
'''
lst = [1, 2, 3, 4, 56]
for n in lst:
    print(n)
    if n == 1:
        continue

lst = [1, 2, 3, 4, 56]
for n in lst:
    if n == 1:
        continue
    print(n)
'''
#Pass
'''
pass --- this is called as space holder
incase any statement like (if, for, else, elif...) this should complete, if not we will get indentation error to avoid this we using pass
'''
'''
for j in range(1, 100):
    pass
'''
 #else - for
'''
It will fall back to else block, when all loops are completed
'''
'''
for m in range(1, 10):
    print(m)
else:
    print("else block")
'''





















