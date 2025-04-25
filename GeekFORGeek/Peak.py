def peak(arr):
    for i in range(1,len(arr)-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            return True
    return False

arr = [1, 2, 4, 5, 7, 8, 3]
print(peak(arr))
# 1 2 4 5 7 8 3