def makeFancyString(str_val: str):
    str_val_arr = list(str_val)
    i=1
    while i <len(str_val_arr)-1:
        if str_val_arr[i] == str_val_arr[i-1]==str_val_arr[i+1]:
            str_val_arr.remove(str_val_arr[i])
        else:
            i+=1

    print("".join(str_val_arr))

str_val = "aaabaaaa"
makeFancyString(str_val)