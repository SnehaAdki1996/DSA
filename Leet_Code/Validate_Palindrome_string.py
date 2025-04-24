import re

def isPalindrome(s1: str):
    str_val = "".join(re.split("[^a-zA-Z0-9]*",s1.lower()))
    return str_val == str_val[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))