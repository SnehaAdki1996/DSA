def firstPalindrome(words) -> str:
    for i in words:
        first = 0
        last = len(i)-1
        while first <= last:
            if i[first] == i[last]:
                first+=1
                last-=1
            if first<last and i[first] != i[last] and i == words[-1]:
                return "---"
            if first<last and i[first] != i[last] :
                break
            if first > last :
                return i


print(firstPalindrome(["xngla","e","itrn","y","s","pfp","rfd"]))


string_main = 'abc'
first = 0
last = len(string_main)-1


while first<=last:
    
    if string_main[first] == string_main[last]:
        first+=1
        last-=1
    else:
        break
    
    if first > last :
        print("palindorme")
    print(first,last)