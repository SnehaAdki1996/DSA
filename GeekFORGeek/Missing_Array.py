arr = [1,2,3,4,6]
actual = [0]*(len(arr)+1)
for i in range(0,len(arr)+1):
    actual[i] = i+1

print(list(set(actual)-set(arr)))
print(actual)