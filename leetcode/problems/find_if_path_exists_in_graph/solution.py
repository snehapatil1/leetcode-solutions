class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges and not n:
            return False
        elif not edges and n == 1:
            return True
        
        visited = [False] * n
        visited[source] = True
        queue = collections.deque()
        node_map = defaultdict(list)
        
        for x, y in edges:
            node_map[x].append(y)
            node_map[y].append(x)
        
        queue.append(source)

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            
            for neighbor in node_map[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return False