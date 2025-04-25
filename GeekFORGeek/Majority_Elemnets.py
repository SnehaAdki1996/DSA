def Majority_Ele(arr):
    hash_map = {}
    for i in range(0,len(arr)):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]]=hash_map[arr[i]]+1
        else:
            hash_map[arr[i]] = 1
    
    for key,val in hash_map.items():
        if val >= len(arr)//2:
            return key
       
    return -1

arr =  [1, 1, 2, 1, 3, 5, 1]
print(Majority_Ele(arr))