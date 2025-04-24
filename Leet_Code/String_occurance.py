def strStr(haystack: str, needle: str):
    return haystack.find(needle)
    for index,i in enumerate(haystack):
        if needle == haystack[index:index+len(needle)]:
            return index
    return -1



print(strStr('mississippi','issip'))




