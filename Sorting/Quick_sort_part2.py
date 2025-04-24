
def quick_sort_rec(arr,low,high):
    pivot = arr[high]

    i = low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j] = arr[j], arr[i]
        
    arr[i+1],arr[high] = arr[high],arr[i+1]

    return i+1

def quick_sort(arr,low,high):
    if low < high:
        pivot_index = quick_sort_rec(arr,low,high)
        print(arr,pivot_index)
        print("--------------------------------")
        quick_sort(arr,low,pivot_index-1)
        quick_sort(arr,pivot_index+1,high)


arr = [8,2,4,7,1,3,9,6,5]
quick_sort(arr,0,len(arr)-1)