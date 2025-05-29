# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


#using sliding window & set
# def lengthOfLongestSubstring(str_val: str) -> int:
#     char_set = set()
#     max_length = 0
#     left = right = 0
#     for right in range(0,len(str_val)):
#         while str_val[right] in char_set:
#             char_set.remove(str_val[left])
#             left+=1
#         char_set.add(str_val[right])
#         max_length = max(max_length,right-left+1)
    
#     print(max_length)

# lengthOfLongestSubstring('pwwkew')
# lengthOfLongestSubstring("abcabcbb")

#using hasmap & sliding window
def lengthOfLongestSubstring_hashmap_sliding(str_val: str) -> int:
    hash_amp = {}
    left = 0
    max_length = 0

    for right in range(0,len(str_val)):
        
        if hash_amp.get(str_val[right]):
            hash_amp[str_val[right]]+=hash_amp[str_val[right]]
        else: 
            hash_amp[str_val[right]] = 1
        
        while hash_amp.get(str_val[right]) > 1:
            hash_amp[str_val[left]] -=1
            left +=1
        max_length = max(max_length , right-left+1)
    
    print(max_length)


print("  using hashmap & Sliding window")
lengthOfLongestSubstring_hashmap_sliding('pwwkew')
lengthOfLongestSubstring_hashmap_sliding("abcabcbb")