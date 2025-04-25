from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        count_a = Counter(a)
        count_b = Counter(b)
    
        for elem in count_b:
            if count_b[elem] > count_a.get(elem, 0):
                return False
        return True
    
a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]
ob = Solution()
print(ob.isSubset(a,b))