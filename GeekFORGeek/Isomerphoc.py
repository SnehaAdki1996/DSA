# Input: s = "egg", t = "add"
# Output: true
# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

def is_siomerphoc(a,b):
    dict_mapping_a = {}
    dict_mapping_b = {}
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] not in dict_mapping_a:
            dict_mapping_a[a[i]] = i
        
        if b[i] not in dict_mapping_b:
            dict_mapping_b[b[i]] = i
        
        if dict_mapping_a[a[i]] != dict_mapping_b[b[i]]:
            return False
    return True
        

a = "babc"
b = "baba"
print(is_siomerphoc(a,b))