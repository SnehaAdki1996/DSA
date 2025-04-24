class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def display(self,root):
        print("1- Inorder")
        print("2- Pre-order")
        print("3- Post-order")
        print("4- Level-order")
        print("Please enter Choice of Display")
        display_ch = int(input())
        if display_ch == 1:
            self.inorder(root)
        elif display_ch ==2:
            self.preOrder(root)
        elif display_ch == 3: 
            self.postOrder(root)
        elif display_ch == 4:
            self.levelOrder(root)


    def levelOrder(self,root):
        pass

    def inorder(self,root):
        if root!=None:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def preOrder(self,root):
        if root!=None:
            print(root.val)
            self.inorder(root.left)
            self.inorder(root.right)

    def postOrder(self,root):
        if root!=None:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.val)

    def add_right(self,root,tempNode):
        if root.val == None:
            root = tempNode
        else:
            temp = root
            while temp.right != None:
                temp = temp.right

            temp.right = tempNode
        return root

    def add_left(self,root,tempNode):
        if root.val == None:
            root = tempNode
        else : 
            temp =root
            while temp.left != None:
                temp = temp.left

            temp.left = tempNode
        return root



if __name__ == '__main__':
    s1 = Solution()
    root = TreeNode()
    ch = 0
    while ch!=3:
        print("-----------------")
        print("Menu")
        print("1) Add Child")
        print("2) Display Tree")
        print("3) Exit")
        print("Enter Choice ")
        ch = int(input())

        if ch == 1:
            print('1) Left Child')
            print('2) Right Child')
            print("Enter Child Option")
            child = int(input())
            print("Enter value of Node")
            value = input()
            temp = TreeNode(value)
            if child == 1:
                root = s1.add_left(root,temp)
            elif child == 2:
                root = s1.add_right(root,temp)

        elif ch == 2:
            s1.display(root)




