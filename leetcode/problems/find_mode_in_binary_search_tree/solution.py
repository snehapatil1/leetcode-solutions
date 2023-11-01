# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        visited = defaultdict(int)
        output = []

        def traverse(root):
            if root:
                visited[root.val] = visited.get(root.val, 0) + 1
                traverse(root.left)
                traverse(root.right)
        
        traverse(root)

        maxFreq = max(visited.values())
        for key in visited.keys():
            if visited[key] == maxFreq:
                output.append(key)
        
        return output