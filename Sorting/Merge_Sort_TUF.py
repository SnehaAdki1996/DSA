# Approach : 

# Approach:

# We will be creating 2 functions mergeSort() and merge().
# mergeSort(arr[], low, high):
# In order to implement merge sort we need to first divide the given array into two halves. Now, if we carefully observe, we need not divide the array and create a separate array, but we will divide the array's range into halves every time. For example, the given range of the array is 0 to 4(0-based indexing). Now on the first go, we will divide the range into half like (0+4)/2 = 2. So, the range of the left half will be 0 to 2 and for the right half, the range will be 3 to 4. Similarly, if the given range is low to high, the range for the two halves will be low to mid and mid+1 to high, where mid = (low+high)/2. This process will continue until the range size becomes.
# So, in mergeSort(), we will divide the array around the middle index(rather than creating a separate array) by making the recursive call :
# 1. mergeSort(arr,low,mid)   [Left half of the array]
# 2. mergeSort(arr,mid+1,high)  [Right half of the array]
# where low = leftmost index of the array, high = rightmost index of the array, and mid = middle index of the array.
# Now, in order to complete the recursive function, we need to write the base case as well. We know from step 2.1, that our recursion ends when the array has only 1 element left. So, the leftmost index, low, and the rightmost index high become the same as they are pointing to a single element.
# Base Case: if(low >= high) return;

def merge_sort(arr,low,high) -> None:
    '''merge & sort the array i/p via low to high'''
    if low>=high:
        return None
    mid = (low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    arr = merge(arr,low,mid,high)
    print(arr)

def merge(arr,low,mid,high) -> list:
    '''sort the i/p between 2 arrays'''
    # for i in range(low,mid):
    #     for j in range(mid+1,high):
    temp = []
    left = low
    right = mid+1
    while left <= mid and right<=high:
        if arr[left]>arr[right]:
            temp.append(arr[right])
            right =right+1
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left = left+1
    
    while left<=mid:
        temp.append(arr[left])
        left = left+1

    while right<=high:
        temp.append(arr[right])
        right =right+1

    
    i = low
    while(i<=high):
        arr[i] = temp[i-low]
        i=i+1
    return arr


merge_sort([4,3,5,6,2,9],0,5)