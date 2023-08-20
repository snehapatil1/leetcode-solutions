"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        queue = collections.deque([node])
        visited = {}
        visited[node] = Node(node.val, [])

        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = Node(neighbor.val, [])
                visited[current_node].neighbors.append(visited[neighbor] )
        
        return visited[node]