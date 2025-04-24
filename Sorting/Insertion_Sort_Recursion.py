def insertion_sort(arr) -> None:
    '''main method of recursion'''
    n = len(arr) / len(arr[0:1])
    rec_insertion(arr,0,n)

def rec_insertion(arr,i,size)->None:
    '''Bubble Via Recursion'''
    if size == i:
        return None
    
    j = i
    while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1],arr[j]
            j = j-1

    print(arr)
    rec_insertion(arr,i+1,size)


insertion_sort([14,6,52,49,94])