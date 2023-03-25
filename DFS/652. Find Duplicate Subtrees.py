# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.output = []
        self.visited = {}

        def dfs(root):
            if not root:
                return ''
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            string = str(root.val) + '.' + left + '.' + right

            if string not in self.visited.keys():
                self.visited[string] = 0
            self.visited[string] += 1
            
            if self.visited[string] == 2:
                self.output.append(root)
            
            return string

        dfs(root)
        return self.output
