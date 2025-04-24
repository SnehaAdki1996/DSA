# Approach

# The algorithm steps are as follows:

# First, we will select the range of the unsorted array using a loop (say i) that indicates the starting index of the range.
# The loop will run forward from 0 to n-1. The value i = 0 means the range is from 0 to n-1, and similarly, i = 1 means the range is from 1 to n-1, and so on.
# (Initially, the range will be the whole array starting from the first index.)
# Now, in each iteration, we will select the minimum element from the range of the unsorted array using an inner loop.
# After that, we will swap the minimum element with the first element of the selected range(in step 1). 
# Finally, after each iteration, we will find that the array is sorted up to the first index of the range. 


def selection_sort(arr: list)-> None:
    """Function used to sort the array by selection sort"""
    for i in range(0,len(arr)):
        min_val = i
        print("---------Iteration ",i,"-----------")
        for j in range(i,len(arr)):
            if arr[min_val]>arr[j]:
                arr[min_val],arr[j] = arr[j],arr[min_val]
            print(arr)
    print(arr)

selection_sort([7, 5, 9, 2, 8])


# ---------Iteration  0 -----------
# [7, 5, 9, 2, 8]
# [5, 7, 9, 2, 8]
# [5, 7, 9, 2, 8]
# [2, 7, 9, 5, 8]
# [2, 7, 9, 5, 8]
# ---------Iteration  1 -----------
# [2, 7, 9, 5, 8]
# [2, 7, 9, 5, 8]
# [2, 5, 9, 7, 8]
# [2, 5, 9, 7, 8]
# ---------Iteration  2 -----------
# [2, 5, 9, 7, 8]
# [2, 5, 7, 9, 8]
# [2, 5, 7, 9, 8]
# ---------Iteration  3 -----------
# [2, 5, 7, 9, 8]
# [2, 5, 7, 8, 9]
# ---------Iteration  4 -----------
# [2, 5, 7, 8, 9]
# [2, 5, 7, 8, 9]
