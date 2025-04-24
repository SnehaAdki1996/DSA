def remDup(arr):
    i = 0
    j = i+1
    while j < len(arr):
        if arr[i]!= arr[j]:
            i =i+1
            arr[i] = arr[j]
        j+=1
    i +=1
    while i < len(arr):
        arr[i] = '_'
        i+=1

arr = [0,0,1,1,1,2,2,3,3,4]
remDup(arr)