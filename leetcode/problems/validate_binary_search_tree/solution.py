# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bfs(node, minVal, maxVal):
            if not node:
                return True
            
            if not (minVal < node.val < maxVal):
                return False
            
            return bfs(node.left, minVal, node.val) and bfs(node.right, node.val, maxVal)
        
        return bfs(root, -float('inf'), float('inf'))

        # def inorder(root):
        #     if not root:
        #         return True
        #     if not inorder(root.left):
        #         return False
        #     if root.val <= self.prev_node:
        #         return False
        #     self.prev_node = root.val
        #     return inorder(root.right)
        
        # self.prev_node = -float('inf')
        # return inorder(root)
        
        
        
        # if root is None:
        #     return False
        
        # queue = collections.deque()
        # queue.append((root, float('inf'), -float('inf')))

        # while queue:
        #     node, maxval, minval = queue.popleft()

        #     if node.val <= minval or node.val >= maxval:
        #         return False
            
        #     if node.left:
        #         if node.left.val < node.val:
        #             queue.append((node.left, node.val, minval))
        #         else:
        #             return False
            
        #     if node.right:
        #         if node.right.val > node.val:
        #             queue.append((node.right, maxval, node.val))
        #         else:
        #             return False
        
        # return True