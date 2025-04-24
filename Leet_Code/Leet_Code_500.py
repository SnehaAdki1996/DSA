# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".


arr1 = ['q','w','e','r','t','y','u','i','o','p']
arr2 = ['a','s','d','f','g','h','j','k','l']
arr3 = ['z','x','c','v','b','n','m']

words = ["Hello","Alaska","Dad","Peace"]

for i in words:
    for each_alp in i:
        if each_alp.lower():
            print(each_alp)
    print('----')

# Output: ["Alaska","Dad"]