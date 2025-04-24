def sub_Sets(arr):
    res = []
    subset = []

    def dfs(i):
        if i >= len(arr):
            res.append(subset.copy())
            return
        
        #to include the left side
        subset.append(arr[i])
        dfs(i+1)

        #not to include
        subset.pop()
        dfs(i+1)

    dfs(0)
    return res

print(sub_Sets([1,2,3]))
