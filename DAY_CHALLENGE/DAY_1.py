def reverseParentheses(s):
    str_list = list(s)
    queue = []
    for i in range(0,len(str_list)):
        if str_list[i] =='(':
            queue.append(i)
        elif str_list[i] == ')':
            str_list[queue[-1]:i+1] = str_list[queue[-1]:i+1][::-1]
            queue.pop()
    
    final_str = ""
    for i in str_list:
        if i not in [')' , '(']:
            final_str = final_str+(i)

    return final_str


reverseParentheses( "(abcd)")