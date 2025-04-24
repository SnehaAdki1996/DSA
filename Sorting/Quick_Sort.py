def quick_sort(arr)->None:
    ''' The sorting happend via piavot element section 
        & we need to place the p[ivaot at the correct position 
        & left to pivot should be smaller & right to pivot should be greater'''
    
    low = 0
    high = len(arr)-1

    qs(arr,low,high)


def qs (arr,low,high):
    if low<high:
        pIndex = rec_qic (arr,low,high)
        qs (arr,low,pIndex-1)
        qs (arr,pIndex+1,high)

def rec_qic(arr,low,high):
    ''' rec call this to sort'''
    i = low -1
    j = high
    pivot = arr[high]
    # if (low < high):
    while i <j:
        while arr[i] <= pivot and i <= high-1:
            i = i+1
            while  arr[j] > pivot and j>=low+1:
                j = j-1
            if i < j :
                arr[i],arr[j] = arr[j],arr[i]
        
        
    arr[low], arr[j] = arr[j],pivot
    print(arr,pivot)
    return j


arr = [90,80,70,60,50,40,30]
quick_sort(arr)