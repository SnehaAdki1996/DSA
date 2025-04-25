def anagram(s1,s2):
    if len(s1) == len(s2):
        s11 = sorted(s1)
        s12 = sorted(s2)
        for i in range(0,len(s1)):
            if s11[i] != s12[i]:
                return False
        return True
        # if s11 == s12:
        #     return True
        # return False
    else:
        return False



s1 = "abcdef"
s2 = "cdefabmn"
print(anagram(s1,s2))