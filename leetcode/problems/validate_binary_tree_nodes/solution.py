class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        children = set(leftChild) | set(rightChild)

        def findRoot():
            for i in range(n):
                if i not in children:
                    return i
            return -1
        
        root = findRoot()
        if root == -1:
            return False
        
        queue = deque([root])
        visited = set()
        visited.add(root)

        while queue:
            node = queue.popleft()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in visited:
                        return False
                    visited.add(child)
                    queue.append(child)
        return n == len(visited)