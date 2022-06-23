# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_dict = {}
        def dfs(node):
            if not node:
                return -1
            level = max(dfs(node.left), dfs(node.right)) + 1
            if level not in level_dict.keys():
                level_dict.update({level:[]})
            level_dict[level].append(node.val)
            return level
        
        dfs(root)
        
        return [level_dict[key] for key in level_dict]