# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.output = []
        self.parentMap = {}
        self.seen = set()
        
        def dfs(node, counter):
            if not node or counter > k or node in self.seen:
                return
            
            self.seen.add(node)
            if counter == k:
                self.output.append(node.val)
            
            dfs(node.left, counter + 1)
            dfs(node.right, counter + 1)
            dfs(self.parentMap[node], counter + 1)
        
        def getParent(node, parent=None):
            if not node:
                return
            self.parentMap[node] = parent
            
            getParent(node.left, node)
            getParent(node.right, node)
        
        getParent(root)
        dfs(target, 0)

        return self.output