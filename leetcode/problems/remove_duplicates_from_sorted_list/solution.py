# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visitedNodes = []
        dummy = head

        prev = head
        while head:
            if head.val not in visitedNodes:
                visitedNodes.append(head.val)
                prev = head
            else:
                prev.next = head.next
            
            head = prev.next
        
        return dummy