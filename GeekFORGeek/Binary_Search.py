def binarysearch(arr, k):
    # Code Here
    low = 0
    high = len(arr)-1
    
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == k and (arr[mid+1]!= k or arr[mid-1]!=k): 
            return mid
        elif arr[mid]<k:
            low = mid+1
        elif arr[mid]>k or arr[mid-1] == k:
            high = mid-1


print(binarysearch([1,1,1,2,2,3,3,3,3,3,3,4,4,4,5,5,5],1))

print(binarysearch([1,2,3,4,5],1))