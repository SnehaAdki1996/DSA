#Match specific pattern
def specific_pattern(n,dict_val,pattern):
    pattern_mached = []
    for each_ele in dict_val:
        if len(each_ele) == len(pattern):
            for i in range(1,len(pattern)):
                if (pattern[i] != pattern [i-1] and each_ele[i] != each_ele[i-1]) or \
                    (pattern[i] == pattern [i-1] and each_ele[i] == each_ele[i-1]):
                    pattern_mached.append(each_ele)
                else:
                    pattern_mached.pop()
                    break
            
    print(set(pattern_mached))
    print(list(set(pattern_mached)))


n = 4 
# abb abc xyz xyy
dict_val = {'abb','abc','xyz','xyy'}
pattern  = 'foo'
specific_pattern(n,dict_val,pattern)