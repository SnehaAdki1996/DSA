# def Smalles_Prime_factor(arr,k):
#     complete_arr=[]
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             complete_arr.append(str(arr[i])+"/"+str(arr[j]))
#             # complete_arr[arr[i]/arr[j]] = arr[i]/arr[j]

#     print(complete_arr)
#     complete_arr.sort()
#     print(complete_arr)
#     print(complete_arr[k-1])
#     print(2/5)

# arr = [1,2,3,5]
# k = 3
# Smalles_Prime_factor(arr,k)



from heapq import heappush, heappushpop


def Smalles_Prime_factor(arr,k):
    arr.sort()
    n = len(arr)
    maxHeap = []      
    for i in range(n) :
        for j in range(i + 1, n) : 
            if len(maxHeap) < k :
                heappush(maxHeap, (- arr[i] / arr[j], i, j))
            else :
                heappushpop(maxHeap, (- arr[i] / arr[j], i, j))
    smallest, i, j = maxHeap[0]
    return (arr[i], arr[j])

arr = [1,2,3,5]
k = 3
Smalles_Prime_factor(arr,k)