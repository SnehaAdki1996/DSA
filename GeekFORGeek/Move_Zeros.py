def move_rezos(nums):

    j=0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j+=1
    while j < len(nums):
        nums[j]=0
        j+=1
    return nums

    # j = 0
    # while j < len(arr):
    #     if arr[j] == 0:
    #         arr.remove(arr[j])
    #         arr.append(0)
    #     j+=1

    # j=0
    # while j < len(arr):
    #     if arr[j] != 0:
    #         j+=1
    #     else:
    #         i = j+1
    #         while i < len(arr):
    #             if arr[i] != 0:
    #                 arr[i],arr[j] = arr[j],arr[i]
    #                 break
    #             else:
    #                 i+=1
    #         j+=1
    print(nums)
    


move_rezos([1,2,4,0,3,0,5,0])


