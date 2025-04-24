def minOperations(logs):
    count = 0
    arr_los = []
    for i in logs:
        if i == './':
            pass
        elif i =='../':
            if  len(arr_los):
                arr_los.pop()
        else:
            arr_los.append(i)
            
    return len(arr_los)


logs = ["./","../","./"]
print(minOperations(logs))
