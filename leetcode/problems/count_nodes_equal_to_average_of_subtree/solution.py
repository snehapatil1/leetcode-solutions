# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def getSubtreeAverage(node):
            nonlocal count
            if not node:
                return 0, 0
            
            leftCount, leftSum = getSubtreeAverage(node.left)
            rightCount, rightSum = getSubtreeAverage(node.right)
            nodeCount = leftCount + rightCount + 1
            nodeSum = leftSum + rightSum + node.val
            
            if node.val == (nodeSum // nodeCount):
                count += 1
            
            return nodeCount, nodeSum
        
        getSubtreeAverage(root)
        return count