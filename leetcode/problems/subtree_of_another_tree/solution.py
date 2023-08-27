# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        
        self.is_same = False

        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            
            if not root or not subRoot or root.val != subRoot.val:
                return False
            
            return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
        
        def preorderTraversal(root):
            if root:
                if root.val == subRoot.val:
                    if dfs(root, subRoot):
                        self.is_same = True
                        return
                preorderTraversal(root.left)
                preorderTraversal(root.right)
        
        preorderTraversal(root)

        return self.is_same