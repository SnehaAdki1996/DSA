def second_smallest(arr,n):
    ''' to get the 2nd smallest'''
    small = float('inf')
    small_2nd = float('inf')
    for i in range(n):
        if arr[i] < small:
            small_2nd = small
            small = arr[i]
        if arr[i] < small_2nd and arr[i] != small:
            small_2nd = arr[i]

    return small_2nd

def second_largest(arr,n):
    ''' to get the 2nd largest'''
    large = float('-inf')
    large_2nd = float('-inf')

    for i in range(n):
        if large < arr[i]:
            large_2nd = large
            large = arr[i]
        if large != arr[i] and arr[i] > large_2nd:
            large_2nd = arr[i]
    return large_2nd


def best_sol_2nd_largest(arr):
    ''' best solution to find 2nd smallest & 2nd largest'''
    n = len(arr)
    sS = second_smallest(arr, n)
    sL = second_largest(arr, n)
    print("Second smallest is", sS)
    print("Second largest is", sL)

best_sol_2nd_largest([1,5,2,27,20])