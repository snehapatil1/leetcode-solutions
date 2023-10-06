# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        lastNode = head
        n = 1

        while lastNode.next:
            n += 1
            lastNode = lastNode.next
        
        index = k % n
        lastNode.next = head
        dummy = head
        
        for i in range(n - index - 1):
            dummy = dummy.next
        
        answer = dummy.next
        dummy.next = None

        return answer