class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = Counter(s)

        for ch in t:
            if ch not in s_counts or s_counts[ch] <= 0:
                return False
            s_counts[ch] -= 1
        
        return sum(s_counts.values()) == 0
