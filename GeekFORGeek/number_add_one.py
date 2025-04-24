def sum_num(arr):
    # str1 = ''
    # for i in arr:
    #     str1 = str1 + str(i)

    # val =  int(str1)+1

    # str_val = str(val)

    carry = 1
    i = len(arr)-1
    while i >= 0:
        sum = arr[i] + carry
        arr[i] = sum % 10
        carry = sum // 10
        i-=1
    
    if carry:
        arr.insert(0,carry)
    return arr
    
# print(sum_num([9]))
print(sum_num([1,9]))
# print(sum_num([1,2,4]))