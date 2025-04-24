def generate(numRows: int):
    arr = []
    for i in range(5):
        sub_arr = []
        for inner_i in range(i+1):
            if inner_i == 0 or inner_i==i:
                sub_arr.append(1)
            else:
                sub_arr.append(arr[i-1][inner_i-1]+arr[i-1][inner_i])
        arr.append(sub_arr)
    return arr[len(arr)-1]

# print(generate(5))


def getRow(rowIndex: int):
        arr = []
        for i in range(rowIndex+1):
            sub_arr = []
            for inner_i in range(i+1):
                if inner_i == 0 or inner_i==i:
                    sub_arr.append(1)
                else:
                    sub_arr.append(arr[i-1][inner_i-1]+arr[i-1][inner_i])
            arr.append(sub_arr)
        return arr[len(arr)-1]


print(getRow(3))