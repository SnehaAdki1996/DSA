def sub_array(arr):
    count = 0
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            if isSub(i,j,arr):
                count+=1
    print(count)


def isSub (start,end,arr):
    prev = 0
    for i in range(0,len(arr)):
        if i <= end and i >= start:
            continue
        if arr[i] <=prev:
            return False
        prev = arr[i]
    return True


nums = [6,5,7,8]

sub_array(nums)