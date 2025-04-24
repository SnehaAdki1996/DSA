def bubbleSort(arr,i,j):
    if i > len(arr)-i or j+1 > len(arr)-1:
        return arr
    else:
        print(j)
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
        bubbleSort(arr,j,j+1)

arr = [5,6,1,3]
for i in range(0,len(arr)):
    # print(arr)
    bubbleSort(arr,i,0)
    print(arr)



print(arr)