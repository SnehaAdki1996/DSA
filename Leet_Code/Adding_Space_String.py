# def addSpaces(str_val, spaces):
#     str_val = list(str_val)
#     for index in range(0,len(spaces)):
#         str_val.insert(index+spaces[index],'_')
#     return ''.join(str_val)


def addSpaces(str_val, spaces):
    final_arr = []
    final_arr.append(str_val[0:spaces[0]])
    for i in range(1,len(spaces)):
        final_arr.append(str_val[spaces[i-1]:spaces[i]])
    final_arr.append(str_val[spaces[-1]:])
    print(final_arr)
    return " ".join(final_arr)

s = "icodeinpython"
spaces = [1,5,7,9]
print(addSpaces(s,spaces))
