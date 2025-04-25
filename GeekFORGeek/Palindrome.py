def Palindrome(str_val):
    reversed = []
    for i in range(len(str_val)-1,-1,-1):
        # print(str_val[i])
        reversed.append(str_val[i])
    reversed_str = ''.join(reversed)

    if reversed_str == str_val:
        return True
    else:
        return False

Palindrome('sneha')