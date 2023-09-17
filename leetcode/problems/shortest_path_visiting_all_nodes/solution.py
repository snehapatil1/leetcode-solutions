class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        visited = set()
        allVisited = (1 << n) - 1
        queue = deque()

        for i in range(n):
            maskValue = (1 << i)
            visited.add((i, maskValue))
            queue.append((i, maskValue, 0))
        
        while queue:
            node, currMaskValue, cost = queue.popleft()
            if currMaskValue == allVisited:
                return cost
            for neighbor in graph[node]:
                bothVisitedMask = currMaskValue | (1 << neighbor)
                if (neighbor, bothVisitedMask) not in visited:
                    visited.add((neighbor, bothVisitedMask))
                    queue.append((neighbor, bothVisitedMask, cost + 1))
        return -1