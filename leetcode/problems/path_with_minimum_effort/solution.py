class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Dijkstra's Algorithm
        rows, cols = len(heights), len(heights[0])
        distance = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        distance[0][0] = 0
        heap = [(0, 0, 0)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        effort = 0

        while heap:
          effort, row, col = heapq.heappop(heap)
          if row == rows - 1 and col == cols - 1:
            return effort
          for x, y in directions:
            nrow, ncol = row + x, col + y
            if 0 <= nrow < rows and 0 <= ncol < cols:
              newEffort = max(effort, abs(heights[row][col] - heights[nrow][ncol]))
              if newEffort < distance[nrow][ncol]:
                distance[nrow][ncol] = newEffort
                heapq.heappush(heap, (newEffort, nrow, ncol))