        
def sorted(nums):
    count = 0
    for i in range(len(nums)):
        print((i-1) % len(nums))
        if nums[(i-1) % len(nums)] > nums[i]:        
            count += 1
        if count > 1:
            return False
    
    return True


print(sorted([13,14,15,11,12]))
