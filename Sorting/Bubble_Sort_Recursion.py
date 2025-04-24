def bubble_sort(arr) -> None:
    '''main method of recursion'''
    rec_bubble(arr,len(arr))

def rec_bubble(arr,size)->None:
    '''Bubble Via Recursion'''
    if size == 1:
        return None
    
    for i in range(0,size-1):
        if arr[i]> arr[i+1]:
            arr[i], arr[i+1] = arr[i+1],arr[i]

    print(arr)
    rec_bubble(arr,size-1)


bubble_sort([14,6,52,49,94])

