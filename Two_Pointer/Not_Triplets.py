def not_triplets(nums,diff):
    nums.sort()
    count=0
    i=0
    while i<len(nums)-1:
        exist = nums[i] +diff
        if exist not in (nums[i:]) or exist+diff not in (nums[i:]):
            count+=1
        i+=1

    print(count)

not_triplets([4,4,2,4,3],3)