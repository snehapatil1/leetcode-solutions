# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        queue = collections.deque()
        queue.append((root, float('inf'), -float('inf')))

        while queue:
            node, maxval, minval = queue.popleft()

            if node.val <= minval or node.val >= maxval:
                return False
            
            if node.left:
                if node.left.val < node.val:
                    queue.append((node.left, node.val, minval))
                else:
                    return False
            
            if node.right:
                if node.right.val > node.val:
                    queue.append((node.right, maxval, node.val))
                else:
                    return False
        
        return True