# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if not root: return inf, -inf
            leftMin, leftMax = dfs(root.left)
            rightMin, rightMax = dfs(root.right)
            curMin, curMax = min(root.val, leftMin, rightMin), max(root.val, leftMax, rightMax)
            self.ans = max(self.ans, root.val - curMin, curMax - root.val)
            return curMin, curMax
        dfs(root)
        return self.ans