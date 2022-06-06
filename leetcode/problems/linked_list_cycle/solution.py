# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        visited_nodes = set()
        while head.next:
            if head in visited_nodes:
                return True
            visited_nodes.add(head)
            head = head.next
        return False
        