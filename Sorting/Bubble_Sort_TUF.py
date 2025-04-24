# Approach 
# The algorithm steps are as follows:

# First, we will select the range of the unsorted array. For that, we will run a loop(say i) that will signify the last index of the selected range. The loop will run backward from index n-1 to 0(where n = size of the array). The value i = n-1 means the range is from 0 to n-1, and similarly, i = n-2 means the range is from 0 to n-2, and so on.
# Within the loop, we will run another loop(say j, runs from 0 to i-1 though the range is from 0 to i) to push the maximum element to the last index of the selected range, by repeatedly swapping adjacent elements.
# Basically, we will swap adjacent elements(if arr[j] > arr[j+1]) until the maximum element of the range reaches the end.
# Thus, after each iteration, the last part of the array will become sorted. Like: after the first iteration, the array up to the last index will be sorted, and after the second iteration, the array up to the second last index will be sorted, and so on.
# After (n-1) iteration, the whole array will be sorted.


def bubble_sort(arr:list)-> None:
    ''' This function used to sort array via bubble sort'''
    for i in range(0,len(arr)):
        print("---------Iteration ",i,"-----------")
        for j in range(0,len(arr)-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            print(arr)
        
    print(arr)


bubble_sort([13,46,26,52,20,9])


# ---------Iteration  0 -----------
# [46, 13, 26, 52, 20, 9]
# [46, 26, 13, 52, 20, 9]
# [46, 26, 52, 13, 20, 9]
# [46, 26, 52, 20, 13, 9]
# [46, 26, 52, 20, 13, 9]
# ---------Iteration  1 -----------
# [46, 26, 52, 20, 13, 9]
# [46, 52, 26, 20, 13, 9]
# [46, 52, 26, 20, 13, 9]
# [46, 52, 26, 20, 13, 9]
# ---------Iteration  2 -----------
# [52, 46, 26, 20, 13, 9]
# [52, 46, 26, 20, 13, 9]
# [52, 46, 26, 20, 13, 9]
# ---------Iteration  3 -----------
# [52, 46, 26, 20, 13, 9]
# [52, 46, 26, 20, 13, 9]
# ---------Iteration  4 -----------
# [52, 46, 26, 20, 13, 9]
# ---------Iteration  5 -----------
# [52, 46, 26, 20, 13, 9]