# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        pass

    def display(self,n):
        while n.left != None or n.right!=None:
            print(n.val)
            

t5 = TreeNode(9)
t4 = TreeNode(5,right=t5)
t3 = TreeNode(0,right=t4)
t2 = TreeNode(-3,right=t3)
root = TreeNode(-10,right=t2)

S1 = Solution()
S1.display(root)



