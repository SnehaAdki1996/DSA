# Approach: 

# Select an element in each iteration from the unsorted array(using a loop).
# Place it in its corresponding position in the sorted part and shift the remaining elements accordingly (using an inner loop and swapping).
# The “inner while loop” basically shifts the elements using swapping.


def insert_sort(arr:list) -> None:
    '''This funciton is used to sort the arr elements via insertion sort method...'''
    for i, val in enumerate(arr):
        print("-------Iteration ",i,"----------")
        for j in range(0,i):
            if val<arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            print(arr)
    print(arr)

insert_sort([13,46,24,52,20,9])


# -------Iteration  0 ----------
# -------Iteration  1 ----------
# [13, 46, 24, 52, 20, 9]
# -------Iteration  2 ----------
# [13, 46, 24, 52, 20, 9]
# [13, 24, 46, 52, 20, 9]
# -------Iteration  3 ----------
# [13, 24, 46, 52, 20, 9]
# [13, 24, 46, 52, 20, 9]
# [13, 24, 46, 52, 20, 9]
# -------Iteration  4 ----------
# [13, 24, 46, 52, 20, 9]
# [13, 20, 46, 52, 24, 9]
# [13, 20, 24, 52, 46, 9]
# [13, 20, 24, 46, 52, 9]
# -------Iteration  5 ----------
# [9, 20, 24, 46, 52, 13]
# [9, 13, 24, 46, 52, 20]
# [9, 13, 20, 46, 52, 24]
# [9, 13, 20, 24, 52, 46]
# [9, 13, 20, 24, 46, 52]
# [9, 13, 20, 24, 46, 52]