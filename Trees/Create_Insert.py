
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def search_element(self,search_ele):
        temp = self
        if temp.data == search_ele:
            return temp
        else:
            for chil in temp.children:
                val = chil.search_element(search_ele)
                if val is not None:
                    return val



if __name__ == '__main__':
    root = TreeNode('Electronics')

    laptop = TreeNode('laptotp')
    cell_phone = TreeNode('Cell Phone')
    Tv = TreeNode('TVS')

    root.add_child(laptop)
    root.add_child(cell_phone)
    root.add_child(Tv)

    Mac = TreeNode('Mac')
    Ms = TreeNode('Ms')
    laptop.add_child(Mac)
    laptop.add_child(Ms)

    Iphone = TreeNode('Iphone')
    Android = TreeNode('Android')
    cell_phone.add_child(Iphone)
    cell_phone.add_child(Android)

    Samsung = TreeNode('Samsung')
    Lg = TreeNode('Lg')
    Tv.add_child(Samsung)
    Tv.add_child(Lg)

    print(root)

    found = root.search_element('Samsung')
    print(found.data)