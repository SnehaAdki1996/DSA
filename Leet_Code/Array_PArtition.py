def Array_par(nums):
    nums.sort()
    sums = 0
    for i in range(0,len(nums),2):
        sums += nums[i]

    print(sums)


Array_par([6,2,6,5,1,2])