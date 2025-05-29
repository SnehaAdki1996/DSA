def long_palin(str_val):
    hash_map = {}
    old_count = 0
    for i in str_val:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1
        if hash_map[i] %2 ==1:
            old_count+=1
        else:
            old_count-=1
    
    if old_count>1:
        return len(str_val) - old_count+1
    return len(str_val)


print(long_palin('abccccdd'))