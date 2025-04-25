# Run Length Encoding

# "wwwwaaadexxxxxx"
def specific(str_val):
    # final_str = str_val[0]+'0'
    final_arr = [str_val[0],1]
    # index_val = 1
    for i in range(1,len(str_val)):
        if str_val[i] == str_val[i-1]:
            final_arr[-1] +=1
        else:
            final_arr[-1] = str(final_arr[-1])
            final_arr.extend([str_val[i],1])
    final_arr[-1] = str(final_arr[-1])
    values = ''.join(final_arr)
    print(values)

str_val = "wwwwaaadexxxxxx"
specific(str_val)