def triplets(nums,diff):
    count= 0
    i = 0
    while i<len(nums)-1:
        exist = nums[i]+diff
        if (exist)in nums[i:] and (exist + diff)  in nums[i:]:
            count+=1
        i+=1
    
    print(count)


triplets([0,1,4,6,7,10],3)