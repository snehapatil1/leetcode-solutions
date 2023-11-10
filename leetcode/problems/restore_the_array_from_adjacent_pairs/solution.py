class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        output = []

        for node1, node2 in adjacentPairs:
            graph[node1].append(node2)
            graph[node2].append(node1)
            indegree[node1] = indegree.get(node1, 0) + 1
            indegree[node2] = indegree.get(node2, 0) + 1
        
        queue = deque()
        for node in indegree:
            if indegree[node] == 1:
                queue.append(node)
                break
        
        visited = set()
        while queue:
            for node in range(len(queue)):
                node = queue.popleft()
                if node in visited:
                    continue
                indegree[node] -= 1
                output.append(node)
                visited.add(node)
                for adj in graph[node]:
                    indegree[adj] -= 1
                    if indegree[adj] <= 1:
                        queue.append(adj)
        
        return output