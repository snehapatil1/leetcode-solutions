# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        def dfs(root, start, total):
            if not root:
                return 0
            
            total -= root.val
            
            if total == 0:
                self.count += 1
            
            dfs(root.left, False, total)
            dfs(root.right, False, total)

            if start:
                dfs(root.left, True, targetSum)
                dfs(root.right, True, targetSum)
            
        dfs(root, True, targetSum)
        
        return self.count
