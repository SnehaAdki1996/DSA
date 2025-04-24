arr = [3,4,5,6,7,8]

xor_sum = 0

for n in arr :
    xor_sum = xor_sum | n

xor_sum = xor_sum * 2 ** (len(arr) - 1) 
print(xor_sum)

# def get_arr(arr):
#     n = len(arr)
#     sublists = []
#     for start in range(n):
#         for end in range(start+1,n+1):
#             print("-------->",start,end)
#             sublists.append(arr[start:end])
#             if start != end-1 and [arr[start],arr[end-1]] not in sublists:
#                 sublists.append([arr[start],arr[end-1]])
#     print(sublists)
    
#     sum = 0
#     for i in sublists:
#         # print(i,end="")
#         sum_arr = 0
#         for j in i:
#             sum_arr = sum_arr ^ j
#         # print(sum_arr)
#         sum=sum+sum_arr
#     print(sum)

# get_arr(arr)