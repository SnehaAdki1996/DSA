    
def max_sub(arr):
    local_max = arr[0]
    global_max = arr[0]
    for i in range(1,len(arr)):
        local_max = max(arr[i],local_max+arr[i])
        
        if global_max < local_max:
            global_max = local_max
            
    return global_max


print(max_sub([1,2,3,-2,5]))