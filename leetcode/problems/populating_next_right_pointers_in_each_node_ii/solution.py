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
    def connect(self, root: 'Node') -> 'Node':
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()
            if queue and queue[0][1] == level:
                node.next = queue[0][0]
            
            if node and node.left:
                queue.append((node.left, level + 1))
            if node and node.right:
                queue.append((node.right, level + 1))
        
        return root