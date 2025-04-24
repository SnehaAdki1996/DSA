def thirdMax(nums):
    nums = list(set(nums))
    nums.sort()
    if len(nums) <3 :
        return nums[-1]
    else:
        return nums[-3]

print(thirdMax([3,2,1]))