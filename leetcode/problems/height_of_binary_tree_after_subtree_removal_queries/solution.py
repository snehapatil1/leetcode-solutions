# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depths = defaultdict(int)

        @cache
        def height(node):
            if not node:
                return 0
            
            return 1 + max(height(node.left), height(node.right))
        
        def dfs(node, depth, maxVal):
            if not node:
                return
            
            depths[node.val] = maxVal
            dfs(node.left, depth + 1, max(maxVal, depth + height(node.right)))
            dfs(node.right, depth + 1, max(maxVal, depth + height(node.left)))
        
        dfs(root, 0, 0)

        return [depths[q] for q in queries]