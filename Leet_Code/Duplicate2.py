# def containsNearbyDuplicate(nums,cons):
#     for i in range(0,len(nums)):
#         for k in range(i+1,len(nums)):
#               if (nums[i] == nums[k]) and abs(i-k)<=cons:
#                     return True
#     return False


# def containsNearbyDuplicate(nums,cons):
#     for i in range(0,len(nums)):
#         try:
#             getindex = nums[i+1:].index(nums[i])+i+1
#             if abs(i -getindex)<=cons:
#                 breakpoint()
#                 return True
#         except ValueError:
#             continue
#     return False
        
def containsNearbyDuplicate(nums,k):
    d = {}
    for i , n in enumerate(nums):
        if n in d and i - d[n] <= k:
            return True
        else: 
            d[n] = i
    return False

nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums,k))