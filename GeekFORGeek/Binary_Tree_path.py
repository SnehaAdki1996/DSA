# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []

        queue = deque([(root,str(root.val))])
        res = []
        while queue:
            node,path = queue.pop()
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                queue.append((node.left,path+"->"+str(node.left.val)))
            if node.right:
                queue.append((node.right,path+"->"+str(node.right.val)))
        print(res)

left1_right = TreeNode(5,None,None)
left1 = TreeNode(2,None,left1_right)
right1 = TreeNode(3,None,None)
r1 = TreeNode(1,left1,right1)

s1 = Solution()
s1.binaryTreePaths(r1)