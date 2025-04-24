def rotate_array(arr,k):
    k = k+1
    res = [0]*len(arr)
    for i in range(len(arr)):
        index = (i+k)%len(arr)
        res[i]=arr[index]

    print(res)

nums = [1,2,3,4,5,6,7]
k = 3
# [5, 6, 7, 1, 2, 3, 4]
# rotate_array(nums,k)



# inplace
nums = [-1]
k = 2
k = k%len(nums)

print(k)
nums = nums[::-1]
l , r = 0,k-1
while l < r:
    nums[l],nums[r] = nums[r],nums[l]
    l+=1
    r-=1

l , r = k,len(nums)-1
while l <r:
    nums[l],nums[r] = nums[r],nums[l]
    l+=1
    r-=1

print(nums)
