def countPairs(nums, target: int):
    count = 0
    nums.sort()
    left =0
    right= len(nums)-1
    while left<right:
        if nums[left]+nums[right] < target: 
            print("----")
            print(left,right)
            count+=right-left
            left+=1
        else:
            right-=1
        # if left ==right:
        #     left+=1
        #     right = len(nums)-1

    print(count)


countPairs(nums= [-6,2,5,-2,-7,-1,3],target=-2)