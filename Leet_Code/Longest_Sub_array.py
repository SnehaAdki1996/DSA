arr = [2,3,5,1,9]
capacity = 10
length = 0

# for i in range(0,len(arr)):
#     sum = 0
#     for j in range(i,len(arr)):
#         # for k in range(i,j+1):
#         sum += arr[j]

#         if sum == capacity:
#             length = max(length,j-i+1)
        
# print(length)


arr = [2,3,5,1,9]
capacity = 10
n = len(arr)
presum = {}
sum = 0 
maxLength = 0


for i in range(0,n):
    sum +=arr[i]
    if sum == capacity:
        maxLength = max(maxLength,i+1)
    rem = sum - capacity
    if rem in presum:
        length = i -presum[rem]
        maxLength = max(maxLength,length)
    if sum not in presum:
        presum[sum] = i

print(maxLength)