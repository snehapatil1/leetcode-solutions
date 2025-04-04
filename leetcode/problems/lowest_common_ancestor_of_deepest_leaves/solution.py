# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.lca, self.deepest = None, 0
        def dfs(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node:
                return depth
            ldepth = dfs(node.left, depth + 1)
            rdepth = dfs(node.right, depth + 1)
            if ldepth == rdepth == self.deepest:
                self.lca = node
            return max(ldepth, rdepth)

        dfs(root, 0)
        return self.lca