# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = deque()
        queue.append((root, 0))

        while queue:
            level_length = len(queue)
            _, cl = queue[0]
            for _ in range(level_length):
                node, l = queue.popleft()

                if node.left:
                    queue.append((node.left, 2*l))
                
                if node.right:
                    queue.append((node.right, 2*l + 1))
            
                max_width = max(max_width, l - cl + 1)

        return max_width