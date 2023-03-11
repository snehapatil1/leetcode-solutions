# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def get_ancestor(self, node, ancestor_map=None):
        if node:
            left = self.get_ancestor(node.left)
            if left:
                ancestor_map.update({left : node.val})
            
            right = self.get_ancestor(node.right)
            if right:
                ancestor_map.update({right : node.val})
        return ancestor_map
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor_map = {}
        ancestor_map = self.get_ancestor(root, ancestor_map)
        p_common_ancestors = []
        while p != root.val:
            if p == q:
                p_common_ancestors.append(p)
            else:
                if p in ancestor_map.keys():
                    p_common_ancestors.append(ancestor_map[p])
                    p = ancestor_map[p]
        while q != root.val:
            if p == q or q in p_common_ancestors:
                return q
            else:
                q = ancestor_map[q]
        
        
