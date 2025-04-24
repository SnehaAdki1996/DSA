# def canMakeSubsequence(str1, str2):
#     for i in str1:
#         final = chr(ord(i)+1)
#         if str2.find(final) >= 0:
#             return True

#     return False

def canMakeSubsequence(source: str, target: str) -> bool:
    targetIdx, targetLen = 0, len(target)  
    for currChar in source:
        if targetIdx < targetLen and (ord(target[targetIdx]) - ord(currChar)) % 26 < 2:
            targetIdx += 1  
    return targetIdx == targetLen

str1 = "ab"
str2 = "d"
print(canMakeSubsequence(str1,str2))