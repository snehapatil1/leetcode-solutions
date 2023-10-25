class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = defaultdict(int)

        for ch in magazine:
            m[ch] = m.get(ch, 0) + 1
        
        for ch in set(ransomNote):
            if ransomNote.count(ch) > m.get(ch, 0):
                return False
        
        return True