def second_largest_BFA(arr):
    arr.sort()
    print("Second Largest via Bruth Force:")
    print("2nd Smallest",arr[1])
    print("2nd Largest",arr[-2])


second_largest_BFA([1,5,2,27,20])


def Second_Largest_Second_Smallest_Best_Approach(arr):
    small = arr[0]
    largest = arr[0]

    for i in range(1,len(arr)):
        if small >= arr[i]:
            small = arr[i]
        if largest < arr[i]:
            largest = arr[i]

    print(small)
    print(largest)

    small_2nd = float('inf')
    largest_2nd = 0
    for i in range(0,len(arr)):
        if  small != arr[i] and small_2nd > arr[i]:
            small_2nd = arr[i]
        if largest != arr[i] and largest_2nd <arr[i]:
            largest_2nd = arr[i]

    print(small_2nd)
    print(largest_2nd)

Second_Largest_Second_Smallest_Best_Approach([1,5,2,27,20])


