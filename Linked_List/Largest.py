arr = [10,20,45,45]


max_1 = 0
max = 0
for i in arr:
    if  max_1 < i and max > i:
        max_1 = i
    if  max < i:
        max = i
    

print(max)
print(max_1)