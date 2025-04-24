def maxCount( banned, n, maxSum):
    sum = 0
    count = 0
    for i in range(1,n+1):
        if i not in banned:
            if sum +i <= maxSum:
                sum = sum + i
                count = count +1  
    print(count)
    return count
    # final_arr = []  
    # sum = 0
    # for i in range(1,n+1):
    #     if i not in banned:
    #         if sum +i <= maxSum:
    #             sum= sum +i
    #             final_arr.append(i) 

    # print(final_arr)
    # print(sum)

banned = [1,6,5]
n = 5
maxSum = 6
maxCount(banned,n,maxSum)