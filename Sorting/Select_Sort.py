
def rec_sel_sort(arr,size):
    if size > len(arr)-1:
        return arr
    mid_in = size
    for j in range(size+1,len(arr)):
        if arr[mid_in] > arr[j]:
            mid_in = j

    arr[mid_in],arr[size] = arr[size],arr[mid_in]
    rec_sel_sort(arr,size+1)

def selection_sort(arr):
    rec_sel_sort(arr,0)
    print(arr)
    # n = len(arr)
    # for i in range(n - 1):
      
    #     # Assume the current position holds
    #     # the minimum element
    #     min_idx = i
        
    #     # Iterate through the unsorted portion
    #     # to find the actual minimum
    #     for j in range(i + 1, n):
    #         if arr[j] < arr[min_idx]:
              
    #             # Update min_idx if a smaller element is found
    #             min_idx = j
        
    #     # Move minimum element to its
    #     # correct position
    #     arr[i], arr[min_idx] = arr[min_idx], arr[i]



selection_sort([64,25,12,22,11])



