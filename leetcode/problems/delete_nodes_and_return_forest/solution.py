# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.output = []
        original_root = root

        def traverse(root):
            if not root:
                return
            
            if root.val in to_delete:
                if root.left and root.left.val not in to_delete:
                    self.output.append(root.left)
                if root.right and root.right.val not in to_delete:
                    self.output.append(root.right)
            
            if root.left:
                traverse(root.left)
                if root.left.val in to_delete:
                    root.left = None
            
            if root.right:
                traverse(root.right)
                if root.right.val in to_delete:
                    root.right = None
        
        traverse(root)
        if original_root.val not in to_delete:
            self.output.append(original_root)
        return self.output