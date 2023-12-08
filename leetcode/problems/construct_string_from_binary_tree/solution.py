# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        preorder = str(root.val)
        if root.left or root.right:
            preorder += f"({self.tree2str(root.left)})"
        if root.right:
            preorder += f"({self.tree2str(root.right)})"
        
        return preorder
        
        # self.preorder = []
        # def preorderTraversal(node):
        #     if not node:
        #         return
            
        #     self.preorder.append(str(node.val))
            
        #     if node.left or node.right:
        #         self.preorder.append("(")
            
        #     if node.left:
        #         preorderTraversal(node.left)
            
        #     if node.left or node.right:
        #         self.preorder.append(")")
            
        #     if node.right:
        #         self.preorder.append("(")
        #         preorderTraversal(node.right)
        #         self.preorder.append(")")
        
        # preorderTraversal(root)
        
        # return "".join(self.preorder)