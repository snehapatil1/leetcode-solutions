class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for frm, to, price in flights:
            graph[frm].append((to, price))
        
        visited = defaultdict(int)
        heap = [(0, k, src)]
        while heap:
            cost, stops, city = heapq.heappop(heap)
            if city == dst:
                return cost
            if stops < 0 or (city in visited and visited[city] >= stops):
                continue
            visited[city] = stops
            for destination, price in graph[city]:
                heapq.heappush(heap, (cost + price, stops - 1, destination))
        return -1