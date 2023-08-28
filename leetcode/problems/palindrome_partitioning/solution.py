class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.combinations = []

        def backtracking(first, curr):
            if first == len(s):
                self.combinations.append(curr[:])
                return
            
            for i in range(first, len(s)):
                sol = s[first : i + 1] 
                if sol == sol[::-1]:
                    backtracking(i + 1, curr + [sol])
            return
        
        backtracking(0, [])
        return self.combinations