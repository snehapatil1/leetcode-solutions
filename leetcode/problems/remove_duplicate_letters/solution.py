class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOccurrence = defaultdict(int)
        stack = []
        visited = set()

        for idx, ch in enumerate(s):
            lastOccurrence[ch] = idx
        
        for idx, ch in enumerate(s):
            if ch not in visited:
                while stack and stack[-1] > ch and lastOccurrence[stack[-1]] > idx:
                    visited.remove(stack.pop(-1))
                
                stack.append(ch)
                visited.add(ch)
        
        return ''.join(stack)