# Given two strings ransomNote and magazine, return true 
# if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

def hash_ftn(str_val):
    my_arr= {}
    for i in str_val:
        if i  not in (list(my_arr.keys())):
            my_arr[i] = 1
        else:
            my_arr[i] =my_arr[i]+1
    return my_arr

def canConstruct(ransomNote: str, magazine: str):
    my_arr_ransom = hash_ftn(ransomNote)
    my_arr_mag = hash_ftn(magazine)
    # if (list(my_arr_ransom.keys())) == (list(my_arr_mag.keys())) and (list(my_arr_ransom.values())) == (list(my_arr_mag.values())):
    #     return True
    # return False
    for k,v in my_arr_ransom.items():
        if my_arr_mag.get(k):
            if my_arr_mag.get(k)<v:    
                return False
        else:
            return False
    return True
    
    

print(canConstruct('aa','aab'))