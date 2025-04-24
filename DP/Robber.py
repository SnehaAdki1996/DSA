arr =[1,2,5,1,3,4]
total_count= [0]*(len(arr))
total_count[0] = arr[0]
total_count[1] = max(arr[0],arr[1])

for i in range(2,len(arr)):
        total_count[i] = max(total_count[i-2]+arr[i],total_count[i-1])

print(total_count[len(arr)-1])