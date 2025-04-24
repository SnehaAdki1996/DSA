# Given an array of strings, group the anagrams together. You can return the answer in any order.

# Input: [“eat”, “tea”, “tan”, “ant”, “bat”]
# Output: [[“bat”], [“ant”, “tan”], [“eat”, “tea”]]

# Input:  [“eat”, “ant”]
# Output: [["eat"],["ant"]]


# output = []
# Output= [[“bat”], [“ant”, “tan”], [“eat”, “tea”]]

from collections import defaultdict
input_arr = ["eat", "tea", "tan", "ant", "bat"]


anagram_groups = {}
print(anagram_groups)

for word in input_arr:
    # Sort the word and use it as the key
    sorted_word = ''.join(sorted(word))
    if sorted_word not in anagram_groups:
        anagram_groups[sorted_word] = []
    anagram_groups.get(sorted_word).append(word)
    
    # Return the grouped anagrams as a list
print(list(anagram_groups.values()))

# dict_output = {}


# for i in range(0,len(input_arr)-1):
#     if i < len(input_arr):
#         key = input_arr[i]
#         val = input_arr[i+1]
#         # mapping_values(input_arr[i],input_arr[i+1])
#         if key not in dict_output.keys() and key not in dict_output.values():
#             dict_output[key] = None
#             if val not in dict_output.keys() and val not in dict_output.values():
#                 dict_output[key] = val

# print(dict_output)
# i = 0 
# j = i+1

# output = []
# while j >= len(input_arr):
#     if sorted(input_arr[i]) == sorted(input_arr[j]):
#         output.append([input_arr[i],input_arr[j]])
#         i = j+1
#         j = i+1
#     else



# def return_anagrams(input_arr):
#     output = []
#     for i in range(0,len(input_arr)):
#         # print(len(input_arr))
#         for j in range(i+1,len(input_arr)):
#             if sorted(input_arr[i]) == sorted(input_arr[j]):
#                 output.append([input_arr[i],input_arr[j]])
#                 # input_arr.remove(input_arr[i])
#                 # input_arr.remove(input_arr[j])
#                 len_arr = len(input_arr)
#                 break
#         else:
#             if input_arr[i] not in output:
#                 output.append([input_arr[i]])
#     return output


# input_arr = ["eat", "tea", "tan", "ant", "bat"]
# print(return_anagrams(input_arr))
    



# Your previous Plain Text content is preserved below:

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you'd like to use for your interview,
# simply choose it from the dots menu on the tab, or add a new language
# tab using the Languages button on the left.

# You can also change the default language your pads are created with
# in your account settings: https://app.coderpad.io/settings

# Enjoy your interview!