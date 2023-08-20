class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        if not graph or len(graph) == 0:
            return paths

        queue = collections.deque()
        current_path = [0]
        queue.append(current_path)
        
        while queue:
            current_node = queue.popleft()
            node = current_node[-1]
            for neighbor in graph[node]:
                temp_path = current_node.copy()
                temp_path.append(neighbor)
                if neighbor == len(graph) - 1:
                    paths.append(temp_path)
                else:
                    queue.append(temp_path)

        return paths