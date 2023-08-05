"""
    Question:
        Given the head of a linked list head, in which each node contains an integer value.
        Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
        Return the linked list after insertion.
        The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        is_gcd = False
        while head:
            if is_gcd:
                is_gcd = False
                head = head.next
            current_val = head.val
            if head.next:
                next_val = head.next.val
                gcd = math.gcd(current_val, next_val)
                new_node = ListNode(gcd)
                new_node.next = head.next
                head.next = new_node
                is_gcd = True
            head = head.next
        
        return dummy.next
