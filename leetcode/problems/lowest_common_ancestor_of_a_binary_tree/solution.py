# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_map = {root: None}
        stack = [root]
        
        while p not in parent_map or q not in parent_map:
            node = stack.pop()
            if node.left:
                parent_map[node.left] = node
                stack.append(node.left)
            if node.right:
                parent_map[node.right] = node
                stack.append(node.right)
        
        p_parents = set()
        while p:
            p_parents.add(p)
            p = parent_map[p]
        
        while q not in p_parents:
            q = parent_map[q]
        
        return q