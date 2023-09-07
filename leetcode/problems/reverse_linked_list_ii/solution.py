# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = dummy.next

        for i in range(1, left):
            prev = prev.next
            curr = curr.next
        
        for i in range(right - left):
            nextNode = curr.next
            curr.next = nextNode.next
            nextNode.next = prev.next
            prev.next = nextNode
        
        return dummy.next
