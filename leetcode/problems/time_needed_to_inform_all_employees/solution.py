class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = defaultdict(list)
        
        # def dfs(boss):
        #     return informTime[boss] + max((dfs(emp) for emp in subordinates[boss]), default=0)
        
        
        # for emp, boss in enumerate(manager):
        #     subordinates[boss].add(emp)
        
        # return dfs(headID)

        for emp, boss in enumerate(manager):
            subordinates[boss].append(emp)
        
        queue = deque([(headID, 0)])
        totalTime = 0

        while queue:
            emp, time = queue.popleft()
            totalTime = max(totalTime, time)
            for subordinate in subordinates[emp]:
                queue.append((subordinate, time + informTime[emp]))
        
        return totalTime