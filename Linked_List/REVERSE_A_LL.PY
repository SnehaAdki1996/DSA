class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add_node(self,head,node):
        if head == None:
            head = node
            return head
        temp = head
        while temp.next!= None:
            temp = temp.next
        temp.next = node
        return head

    def dispay(self,head):
        temp = head
        while temp!= None:
            print("{}->{}".format(temp.val,temp.next))        
            # print(temp.val)
            # print(temp.next)
            temp = temp.next

    # def reverse(self,head):
    #     prev, cur  = None,head

    #     while cur:
    #         temp = cur.next
    #         cur.next = prev
    #         prev,cur = cur,temp

    #     return prev

    def reverse(self,head):
        prev,cur = None , head

        while cur:
            temp = cur.next
            cur.next = prev
            prev,cur = cur, temp
        
        return prev

i = 0
head = None
main = ListNode()
while i<5:
    l1 = ListNode(input("Enter number"))
    head= main.add_node(head,l1)
    i+=1

main.dispay(head)

head = main.reverse(head)
main.dispay(head)


temp = head
while temp:
    if temp.val < temp.next.val:
        temp.next = temp.next.next
    temp = temp.next


main.dispay(head)