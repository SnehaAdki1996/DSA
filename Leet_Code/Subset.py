n = [1,6,20,7,8]
# True

def sum_val(i,j):
    mid =  (0+j)//2
    print(i,j,mid)
    sum = 0
    for itr in range(0,mid):
        sum += n[itr]
    sum2 = 0
    for itr in range(mid,j):
        sum2 += n[itr]
    print(n[i:mid],n[mid:j+1])
    print(sum,sum2)
    if sum == sum2:
        return True
    else:
        n[mid],n[mid+1] = n[mid+1],n[mid]
        sum_val(0,len(n))
        return False

i = 0
j = len(n)

print(sum_val(i,j))
# while i<j:
#     sum(i,j)
    # i+=1





