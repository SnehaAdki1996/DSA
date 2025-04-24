def sort_0_1_2(arr):
    j =0
    # for i in range(0,len(arr)):
    #     for j in range(i,len(arr)):
    #         if arr[i] > arr[j]:
    #             arr[i],arr[j] = arr[j],arr[i]
    # print(arr)
    while j < len(arr)-1:
        if arr[j]==0:
            arr.pop(j)
            arr.insert(0,0)
            j+=1
        elif arr[j] == 2:
            arr.pop(j)
            arr.insert(len(arr)-1,2)
            if j == len(arr)-2:
                j+=1
            # j+=1
        else:
            j+=1
    print(arr)


arr = [0, 1, 2, 0, 1, 2]
# 12012
# 012012

# 01012
# 01012 2


sort_0_1_2(arr)