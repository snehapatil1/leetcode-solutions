class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for x, y, d in times:
            graph[x].append((d, y))
        
        visited = set()
        time = 0
        heap = [(0, k)]
        heapq.heapify(heap)
        while heap:
            cost, node = heapq.heappop(heap)
            if node not in visited:
              visited.add(node)
              time = max(time, cost)
              for c, neighbor in graph[node]:
                  if neighbor not in visited:
                      heapq.heappush(heap, (c + cost, neighbor))
        
        return time if len(visited) == n else -1
