def getSecondLargest( arr):
    # Code Here
    # arr.sort()
    # return arr[-2]
    fg = sg = 0
    for i in range(0,len(arr)):
        if arr[i] > fg:
           sg = fg 
           fg = arr[i]
        elif arr[i] > sg and arr[i]!= fg:
           sg = arr[i]
       
            
    return sg

getSecondLargest([10,5,10])