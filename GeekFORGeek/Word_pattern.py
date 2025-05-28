
def wordPattern(pattern: str, s: str):
    words_arr=s.split(" ")
    if len(pattern) != len(words_arr):
        return False
    dict_ptn = {}
    dict_words = {}
    for i in range(len(pattern)):
        if pattern[i] not in dict_ptn:
            dict_ptn[pattern[i]] = i

        if words_arr[i] not in dict_words:
            dict_words[words_arr[i]] = i

        if dict_words[words_arr[i]] != dict_ptn[pattern[i]]:
            return False
    
    return True
            

pattern = "abba"
s = "dog cat catt dog"
wordPattern(pattern,s)
