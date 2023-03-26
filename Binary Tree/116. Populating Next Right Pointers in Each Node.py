"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]', n=None) -> 'Optional[Node]':
        if not root:
            return
        
        root.next = n

        self.connect(root.left, root.right)
        self.connect(root.right, n.left if n else None)

        return root
