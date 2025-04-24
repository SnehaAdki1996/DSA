class ListNode:
    def __init__(self,val = 0,next = None) -> None:
        self.val = val
        self.next = None
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

    def doubleIt(self, head):
        str_num = ''
        temp = head 
        while temp!=None:
            str_num = str_num +temp.val
            temp = temp.next
        
        double = int(str_num)*2
        doube_str = str(double)
        
        new_head = ListNode(0)
        temp = new_head
        for i in doube_str:
            temp.next =  ListNode(i)
            temp = temp.next

        return new_head.next
i = 0
head = None
main = ListNode()
while i<3:
    l1 = ListNode(input("Enter number"))
    head= main.add_node(head,l1)
    i+=1

main.dispay(head)

head = main.doubleIt(head)

main.dispay(head)


