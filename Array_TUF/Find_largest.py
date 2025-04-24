def get_largest(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if max < arr[i]:
            max = arr[i]
    print("Normal Approach: ",max)


get_largest([1,5,2,7,20])


def bruthForce(arr):
    arr.sort()
    print("Bruth Force Approach: ",arr[-1])

bruthForce([1,5,2,7,20])


def rec(arr):
    max  =0
    for i in range(0,len(arr)):
        max = rec_max(max,arr[i])

    print("Recrussive Approach: ",max)


def rec_max(max,ele):
    return max if max > ele else ele


rec([1,5,2,7,20])