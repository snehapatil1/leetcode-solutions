# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = head
        prev = None
        while dummy:
            next_node = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = next_node
        return prev