# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = collections.defaultdict(list)
        queue = collections.deque([root])
        seen = set()

        while queue:
            # create graph with each node as key and all adjacent nodes as values and direction to reach those adjav=cent nodes
            # graph = {'3': [('1', 'U')]}
            node = queue.popleft()

            if node.left:
                graph[node.left.val].append((node.val, "U"))
                graph[node.val].append((node.left.val, "L"))
                queue.append(node.left)
            
            if node.right:
                graph[node.right.val].append((node.val, "U"))
                graph[node.val].append((node.right.val, "R"))
                queue.append(node.right)
        
        # create new queue to start from start value and path as ""
        queue = collections.deque([(startValue, "")])

        while queue:
            cur_val, cur_path = queue.popleft()

            # if current node was already visited then continue to next node
            if cur_val in seen:
                continue
            
            # add current node to visited list
            seen.add(cur_val)
            
            if cur_val == destValue:
                return cur_path
            else:
                # get all adjacent nodes for the current node
                for child, destination in graph[cur_val]:
                    if child not in seen:
                        # if adjacent child node is not visited then add this child in queue and update path with that direction
                        queue.append((child, cur_path + destination))
