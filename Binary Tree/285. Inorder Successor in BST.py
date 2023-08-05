"""
    Question:
        Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. 
        If the given node has no in-order successor in the tree, return null.
        The successor of a node p is the node with the smallest key greater than p.val.
"""

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
