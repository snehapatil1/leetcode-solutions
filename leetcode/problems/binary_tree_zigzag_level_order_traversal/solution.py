# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        
        output = []

        # move from left to righy
        is_left_to_right = True

        # initialize queue with 1st node
        queue = [root]

        while queue:
            # current level of nodes
            level = []

            # for current node
            for i in range(len(queue)):
                # remove 1st element from queue
                node = queue.pop(0)
                # add value of node from queue to level
                level.append(node.val)

                # if node has left child then add that child in queue
                if node.left:
                    queue.append(node.left)
                
                # if node has right child then add that child in queue
                if node.right:
                    queue.append(node.right)
                
            # if is_left_to_right is set to False then reverse the level
            if not is_left_to_right:
                level.reverse()
            
            # reverse boolean value of is_left_to_right for next iteration
            is_left_to_right = not is_left_to_right
            # add final level in output
            output.append(level)
        
        return output