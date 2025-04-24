# i != j indices
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# return True if above condition matches

def checkIfExist(arr):
    seen =set()
    for i in range(0,len(arr)):
        if arr[i] * 2 in seen or arr[i] / 2 in seen:
            return True
        seen.add(arr[i])
            
    return False


arr = [16,-13,8]
print(checkIfExist(arr))
