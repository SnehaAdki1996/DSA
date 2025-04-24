str_val = 'dabab'


# l,r = 0,len(str_val)-1
# while l < len(str_val) and r > 0 and str_val[l] == str_val[r]:
#     l += 1 
#     r -= 1
#     print("Palindrome")

# if l < len(str_val) and r > 0 and str_val[l] != str_val[r]:
#     print("Not Palindrome ")


res = ""
resLen = 0

for i in range(len(str_val)):

    l,r = i,i
    while l>=0 and r <len(str_val) and str_val[l] == str_val[r]:
        if resLen < (r-l+1):
            res = str_val[l:r+1]
            resLen = r-l+1
        l-=1
        r+=1

    l,r = i,i+1
    while l >=0 and r < len(str_val) and str_val[l] == str_val[r]:
        if resLen < (r-l+1):
            res = str_val[l:r+1] 
            resLen = r-l+1
        i-=1
        r+=1

print(res,resLen)
        
