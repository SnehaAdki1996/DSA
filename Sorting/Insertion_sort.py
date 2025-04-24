# def insertSort(arr):
#     for i in range(1,len(arr)):
#         j = i-1
#         key = arr[i]

#         while j >= 0 and key < arr[j]:
#             arr[j+1]=arr[j]
#             j-=1

#         arr[j+1] = key
def rec_in(arr,size):
    if size > len(arr)-1:
        return arr
    key = arr[size]
    j = size-1
    while j>=0 and key < arr[j]:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1]= key
    rec_in(arr,size+1)


def insertSort(arr):
    rec_in(arr,1)
    print(arr)



insertSort([12,11,13,5,6])