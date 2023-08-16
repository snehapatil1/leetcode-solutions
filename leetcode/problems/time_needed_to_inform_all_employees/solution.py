class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = defaultdict(set)
        
        def dfs(boss):
            return informTime[boss] + max((dfs(emp) for emp in subordinates[boss]), default=0)
        
        
        for emp, boss in enumerate(manager):
            subordinates[boss].add(emp)
        
        return dfs(headID)