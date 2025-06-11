# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def create_node(self, new_l, val):
        node = ListNode(val)
        node.next = None
        new_l.next = node
        new_l = new_l.next
        return new_l
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        new_list = dummy
        carry = 0

        while l1 or l2:
            l1_num = l1.val if l1 else 0
            l2_num = l2.val if l2 else 0

            new_num = l1_num + l2_num + carry
            if new_num > 9:
                carry = new_num // 10
                new_num = new_num % 10
            else:
                carry = 0
            
            dummy = self.create_node(dummy, new_num)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            dummy = self.create_node(dummy, carry)

        return new_list.next