def findMaxK(nums):
    max = 0
    for i in range(0,len(nums)):
        if max < nums[i]:
            for j in range(0,len(nums)):
                if nums[i] == -nums[j]:
                    max= nums[i]

    if max ==0:
        return -1
    return max

print(findMaxK([-3,13,1,-15]))