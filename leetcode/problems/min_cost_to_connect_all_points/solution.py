class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        pointsMap = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                pointsMap[i].append((distance, j))
                pointsMap[j].append((distance, i))
        
        output = 0
        counter = 0
        visited = [0] * n
        visited[0] = 1
        heap = pointsMap[0]
        heapq.heapify(heap)

        while heap:
            dist, point = heapq.heappop(heap)
            if not visited[point]:
                visited[point] = 1
                counter += 1
                output += dist
                for p in pointsMap[point]:
                    heapq.heappush(heap, p)
            if counter >= n:
                break
        
        return output