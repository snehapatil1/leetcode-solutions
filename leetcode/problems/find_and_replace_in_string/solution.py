class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        for i, src, tar in sorted(list(zip(indices, sources, targets)), reverse=True):
            if s[i:i+len(src)] == src:
                s = s[:i] + tar + s[i+len(src):]
        
        return s