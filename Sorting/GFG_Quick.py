

def quickSort(arr,low,high):
    if low<high:
        pIndex = partition (arr,low,high)
        quickSort (arr,low,pIndex-1)
        quickSort (arr,pIndex+1,high)

def partition(arr,low,high):
    ''' rec call this to sort'''
    pivot = arr[high]
    i = low - 1
    # j = high
    for j in range(low,high):
        if arr[j]<= pivot:
            i=i+1
            (arr[i],arr[j]) = (arr[j],arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    print(arr,pivot)
    return i+1


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, len(data) - 1)

print('Sorted Array in Ascending Order:')
print(data)
