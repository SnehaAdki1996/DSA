
from collections import deque
class Node:
    def __init__ (self,val):
        self.data = val
        self.left = None
        self.right = None

class TreeData:
    def __init__(self):
        self.root = None

    def add_child(self,new_node):
        if self.root == None:
            self.root = new_node
        else:
            temp = self.root
            queue = deque([temp])
            while queue:
                poped = queue.popleft()

                if poped.left is None:
                    poped.left = new_node
                    break
                else:
                    queue.append(poped.left)
                
                if poped.right is None:
                    poped.right = new_node
                    break
                else:
                    queue.append(poped.right)


    def delete_node(self,val):
        if (self.root == None):
            return self
        queue = deque([self.root])
        target = None

        while queue:
            temp = queue.popleft()
            if temp.data == val:
                target = temp
                break
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        if target == None:
            return self
        
        queue = deque([(self.root,None)])
        last_node = None
        last_parent = None

        while queue:
            curr,parent = queue.popleft()
            last_node = curr
            last_parent = parent

            if curr.left:
                queue.append((curr.left,curr))
            if curr.right:
                queue.append((curr.right,curr))

        target.data = last_node.data

        if last_parent:
            if last_parent.left == last_node:
                last_parent.left = None
            else:
                last_parent.right = None

        return self

    def traverse_bfs(self):
        temp = self.root
        queue = ([temp])
        while queue:
            poped = queue.pop(0)
            print(poped,poped.left,poped.data,poped.right, end="\n")
            if poped.left:
                queue.append(poped.left)
            if poped.right:
                queue.append(poped.right)

    def traverse_dfs_inorder(self,node):
        if node is None:
            return
        self.traverse_dfs_inorder(node.left)
        print(node.root.data,end=" ")
        self.traverse_dfs_inorder(node.right)

    def traverse_dfs_preorder(self,node):
        if node is None:
            return 
        print(node.data,end=" ")
        self.traverse_dfs_preorder(node.left)
        self.traverse_dfs_preorder(node.right)


    def traverse_dfs_postorder(self,node):
        if node is None:
            return
        self.traverse_dfs_postorder(node.left)
        self.traverse_dfs_postorder(node.right)
        print(node.root.data,end=" ")



root_tree = TreeData()
# root_tree.root = Node(10)
ch = 0
while ch!=7:
    print("-----------------")
    print("Menu")
    print("1) Insert")
    print("2) Travesal Tree BFS")
    print("3) Travesal Tree DFS (pre-order)")
    print("4) Travesal Tree DFS (post-order)")
    print("5) Travesal Tree DFS (in-order)")
    print("6) Delete")
    print("7) Exit")
    print("Enter Choice ")
    ch = int(input())

    if ch == 1:
        val = input(print("Enter value for node"))
        new_node = Node(val)
        root_tree.add_child(new_node)
    elif ch == 2:
        root_tree.traverse_bfs()
    elif ch == 3:
        root_tree.traverse_dfs_preorder(root_tree.root)
    elif ch == 4:
        root_tree.traverse_dfs_postorder(root_tree.root)
    elif ch == 5:
        root_tree.traverse_dfs_inorder(root_tree.root)
    elif ch == 6:
        val = input(print("Enter value you want to delete"))
        root_tree.delete_node(val)
