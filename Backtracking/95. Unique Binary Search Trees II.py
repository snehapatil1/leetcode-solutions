"""
  Question:
    Given an integer n, return all the structurally unique BST's (binary search trees), 
    which has exactly n nodes of unique values from 1 to n. 
    Return the answer in any order.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def generate_trees(l, r):
            return [None] if l > r else [
                TreeNode(val, left, right)
                for val in range(l, r + 1)
                for left in generate_trees(l, val - 1)
                for right in generate_trees(val + 1, r)
            ]
        
        # generate trees with root as every number from 1 to n
        return generate_trees(1, n)
