def minHeight(arr,k):
    n = len(arr)

    arr.sort()
    ans = arr[n-1]-arr[0]
    
    for i in range(1,n):
        shortest = min(arr[0]+k,arr[i]-k)
        longest = max(arr[n-1]-k,arr[i-1]+k)
        final = min(ans,longest-shortest)

    return final
arr=[1,5,8,10]
k = 2
val = minHeight(arr,k)
print(val)