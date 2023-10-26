# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode(0)
        dummy = newList
        total, carry = 0, 0

        while l1 or l2:
            num1 = int(l1.val) if l1 else 0
            num2 = int(l2.val) if l2 else 0
            
            res = (num1 + num2)
            if carry > 0:
                res += carry
                carry = 0
            
            total = res % 10
            carry = res // 10

            node = ListNode(total)
            dummy.next = node
            dummy = node

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        
        if carry > 0:
            node = ListNode(carry)
            dummy.next = node
            dummy = node
        
        return newList.next