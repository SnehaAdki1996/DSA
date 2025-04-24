def singleNumber(nums):
    hashmap = {}
    for ele in nums:
        hashmap[ele] = hashmap.get(ele,0)+1

    for ele in hashmap:
        if hashmap[ele] == 1:
            return ele

nums = [4,1,2,1,2]
print(singleNumber(nums))