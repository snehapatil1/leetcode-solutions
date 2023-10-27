# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        nodes = 1
        queue = deque([root])

        while queue:
            level = []
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                level.append(node.left)
            if node.right:
                queue.append(node.right)
                level.append(node.right)
            nodes += len(level)
        
        return nodes
