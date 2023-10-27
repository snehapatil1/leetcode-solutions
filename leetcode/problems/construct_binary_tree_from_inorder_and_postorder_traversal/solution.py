# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        node = TreeNode(postorder.pop())
        index = inorder.index(node.val)
        node.right = self.buildTree(inorder[index + 1:], postorder)
        node.left = self.buildTree(inorder[:index], postorder)
        return node