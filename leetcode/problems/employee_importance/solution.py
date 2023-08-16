"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total_importance = 0
        subordinates = []
        hash_set = {e.id:e for e in employees}

        def dfs(employee, subordinates, total_importance):
            total_importance += hash_set[employee].importance
            for subordinate in subordinates:
                total_importance = dfs(subordinate, hash_set[subordinate].subordinates, total_importance)
            return total_importance
    
        for employee in hash_set:
            if employee == id:
                total_importance = dfs(employee, hash_set[employee].subordinates, total_importance)

        return total_importance