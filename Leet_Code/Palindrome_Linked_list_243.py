class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert_node(self,val,head):
        new_node = ListNode(val)
        if head is None:
            head = new_node
        else:
            t1 = head
            while t1.next != None:
                t1= t1.next
            t1.next = new_node
        return head

    def print_node(self,head):
        t1 = head
        while t1 != None :
            print(str(t1.val)+"------>"+str(t1.next))
            t1 = t1.next

    def isPalindrome(self, head):
        t1 = head
        arr = []
        while t1 != None:
            arr.append(t1.val)
            t1 = t1.next
        return True if arr == arr[::-1] else False 

    def Reverse(self, head):
        temp = head
        while temp != None:
            print(str(temp.val)+"------>"+str(temp.next))
            temp = temp.next

        prev = None
        curr = head
        while curr  != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head = prev
        return head

    def Remove_Duplicate(self,head):
        temp = head
        while temp.next != None:
            if temp.val == temp.next.val:
                temp.next=temp.next.next
            else:
                temp = temp.next
        return head

    def Reorder_List(self,head):

        ## Find the middle
        p1 = head
        p2 = head
        while (p1.next != None and  p2 != None) and p2.next.next != None :
            p1 = p1.next
            p2 = p2.next.next
            if p2.next == None:
                break
            print(p1,p2)
            self.print_node(head)
            

        # here p2 will be my mid

        # reversed the Link List
        preMid = p1 
        preCurr = p1.next
        while preCurr.next!=None:
            curr = preCurr.next
            preCurr.next = curr.next
            curr.next = preMid.next
            preMid.next = curr

        t1 = head
        t2 = preMid.next

        # join alternately
        while t1 != preMid:
            preMid.next = t2.next
            t2.next = t1.next 
            t1.next = t2
            t1 = t2.next
            t2= preMid.next

        return head


if __name__ == '__main__':
    s1 = Solution()
    head = None
    while True:
        print("Choises are")
        print("1: Insert Node")
        print("2: Delete Node")
        print("3: Print Node")
        print("4: Check Palindrome")
        print("5: Reverse")
        print("6: Remove Duplicate")
        print("7: Reorder List")
        print("8: Exit")

        choice = int(input("Please Enter you Choice"))
        if choice == 1:
            head = s1.insert_node(int(input("Enter Value You want to insert")),head)
        elif choice == 2:
            print("Deleted")
        elif choice == 3:
            s1.print_node(head)
        elif choice == 4:
            print(s1.isPalindrome(head))
        elif choice == 5:
            head = s1.Reverse(head)
            print("After reverse the list is")
            s1.print_node(head)
        elif choice == 6:
            head = s1.Remove_Duplicate(head)
            print("After reverse the list is")
            s1.print_node(head)
        elif choice == 7:
            head = s1.Reorder_List(head)
            print("After Reorder the list is")
            s1.print_node(head)
        else:
            break

