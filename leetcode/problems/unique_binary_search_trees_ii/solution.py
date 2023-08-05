# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def generate_trees(l, r):
            return [None] if l > r else [
                TreeNode(val, left, right)
                for val in range(l, r + 1)
                for left in generate_trees(l, val - 1)
                for right in generate_trees(val + 1, r)
            ]
        
        return generate_trees(1, n)