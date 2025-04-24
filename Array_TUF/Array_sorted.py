def check_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            return False
        
    return True

if check_sorted([1,8,3,4,5]):
    print("Sorted")
else:
    print("Not Sorted")