# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        inorder = []
        
        def inorderTraversal(root, inorder):
            if not root:
                return []
            
            inorder = inorderTraversal(root.left, inorder)
            inorder.append(root.val)
            inorder += inorderTraversal(root.right, inorder)

            return inorder
        
        inorder = inorderTraversal(root, inorder)
        p_index = inorder.index(p.val)
        
        return TreeNode(inorder[p_index + 1]) if inorder[-1] != inorder[p_index] else None
