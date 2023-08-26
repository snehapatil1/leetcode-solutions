# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create_BST(arr, start, end):
            if end < start:
                return None
            
            mid = (start + end) // 2
            root = TreeNode(arr[mid])
            root.left = create_BST(arr, start, mid - 1)
            root.right = create_BST(arr, mid + 1, end)
            return root

        
        return create_BST(nums, 0, len(nums) - 1)
