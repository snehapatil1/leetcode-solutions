# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nlen = 0
        dummy = head
        while dummy:
            nlen += 1
            dummy = dummy.next
        
        removeidx = nlen - n
        if not removeidx:
            return head.next
        
        cnt = 0
        prev = None
        curr = head
        while head:
            if cnt == removeidx:
                prev.next = head.next
            prev = head
            head = head.next
            cnt += 1
        return curr