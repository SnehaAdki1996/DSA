
def leaders( arr):
    # code here
    leader = []
    
    leader.append(arr[-1])
    for i in range(len(arr)-2,-1,-1):
        print(arr[i])
        if leader[-1] <= arr[i]:
            leader.append(arr[i])
    return leader[::-1]
    
arr =[61,61,17]
print(leaders(arr))