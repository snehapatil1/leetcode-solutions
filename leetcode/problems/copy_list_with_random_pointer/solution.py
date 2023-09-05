"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        mapping = defaultdict()
        
        curr = head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            mapping[curr].next = mapping.get(curr.next, None)
            mapping[curr].random = mapping.get(curr.random, None)
            curr = curr.next
        
        return mapping[head]