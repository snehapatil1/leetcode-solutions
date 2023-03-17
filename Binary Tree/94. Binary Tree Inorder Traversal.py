# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        if root:
            output = self.inorderTraversal(root.left)
            output.append(root.val)
            output += self.inorderTraversal(root.right)

        return output
