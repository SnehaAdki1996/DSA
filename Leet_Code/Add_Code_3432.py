def nums_sum_even(nums):
    count = 0
    for i in range(0,len(nums)):
        if (sum(nums[0:i+1]) - sum(nums[i+1:len(nums)]))%2 ==0 and len(nums[0:i+1]) > 0 and len(nums[i+1:len(nums)]) > 0: 
            count+=1
    return count
    

# def sum(a1,a2):
#     sum1 = lambda x:
#     print(a1)
#     print(a2)
#     pass

nums = [10,10,3,7,6]
print(nums_sum_even(nums))

