# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest_nums = []

        smallest_nums = self.dfs(root, smallest_nums)
        smallest_nums.sort()

        return smallest_nums[k-1]
        
            
    def dfs(self, root, smallest_nums):
        if not root:
            return []
        
        smallest_nums = self.dfs(root.left, smallest_nums)
        smallest_nums.append(root.val)
        smallest_nums += self.dfs(root.right, smallest_nums)

        return smallest_nums
