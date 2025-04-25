def duplicate_sorted(arr):
    unique_index = 1
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr[unique_index] = arr[i]
            unique_index+=1
            
    return unique_index

arr =[1,1,2,3,4,5,5]
len_val = duplicate_sorted(arr)
print(arr[:len_val])
arr1 = [2, 2, 2, 2, 2]
len_val = duplicate_sorted(arr1)
print(arr1[:len_val])