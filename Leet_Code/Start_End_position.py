def searchRange(nums, target):
    final = []
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         if len(final) == 0:
    #             final.append(i)

    i = 0
    j = len(nums)-1

    while i != len(nums)-1 and j != 0 :
        if nums[i] == target:
            final.append(i)
            i = len(nums)-1
        if nums[j] == target:
            final.append(j)
            j = 0
        if nums[i] != target:
            i += 1
        if nums[j] != target:
            j-=1
    print(final)


searchRange([5,7,7,8,8,8,10],8)