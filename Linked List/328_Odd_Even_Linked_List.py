# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        # initialise odd and even nodes to 0 and add those nodes in oddHead and evenHead linked list
        odd = ListNode(0)
        even = ListNode(0)
        oddHead = odd
        evenHead = even
        
        # initialise isEven to false to start with 1st node which will be odd
        isEven = False
        
        while head:
            if isEven:
                # if even node then current even node's next will be current head which is even
                # set current even as current head
                even.next = even = head
            else:
                # if odd node then current odd node's next will be current head which is odd
                # set current odd as current head
                odd.next = odd = head

            # toggle isEven for next node
            isEven = not isEven
            head = head.next
        
        # last node of even must be None
        even.next = None
        # last node of odd must be 2nd node of even as we started from 0
        odd.next = evenHead.next
        
        # return 2nd node of odd as we started from 0
        return oddHead.next
