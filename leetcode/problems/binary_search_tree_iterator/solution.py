# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.ino = []
        self.currIndex = -1
        self.inorder(root)
        self.n = len(self.ino)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.ino.append(root.val)
            self.inorder(root.right)
            return root
        

    def next(self) -> int:
        self.currIndex += 1
        return self.ino[self.currIndex]

    def hasNext(self) -> bool:
        if self.currIndex + 1 < self.n:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()