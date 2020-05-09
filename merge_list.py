#Merge Two sorted linked lists and return it as a new list.
# The new new list should be made by splicing together the nodes of the first two lists

#Assume lists are not empty and contain integer values

#Input: 1,3,4  4,5,3
#Output: 1,3,3,4,4,5

#Time complexity 0(n)and space of 0(1)

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        head = p1 #saves the head of list
               
        while p1 and p2:
            if p1.val < p2.val:
                if not p1.next:
                    p1.next = p2
                    break
                else:
                    p1 = p1.next
            else:
                tmp = ListNode(p1.val)
                tmp.next = p1.next
                p1.val = p2.val
                p1.next = tmp
                if not p1.next:
                    p1.next = p2.next
                    break
                p2 = p2.next      
        
        return head if head else p2# if p1 is null