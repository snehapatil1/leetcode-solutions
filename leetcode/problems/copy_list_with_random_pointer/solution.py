"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited = {}

    def getClonedNode(self, node):
        if not node:
            return None
        
        if node in self.visited:
            return self.visited[node]
        
        new_node = Node(node.val, None, None)
        self.visited[node] = new_node
        return new_node

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        old_list = head
        new_list = Node(old_list.val, None, None)
        self.visited[old_list] = new_list

        while old_list:
            next_node = self.getClonedNode(old_list.next)
            random_node = self.getClonedNode(old_list.random)
            new_list.next = next_node
            new_list.random = random_node
            old_list = old_list.next
            new_list = new_list.next
        
        return self.visited[head]