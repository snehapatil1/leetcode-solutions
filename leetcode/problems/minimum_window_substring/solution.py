class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '' or len(s) < len(t):
            return ''
        
        counter_t = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(counter_t)
        res, resLen = [-1, -1], float('inf')

        left = 0
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in counter_t and window[ch] == counter_t[ch]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                window[s[left]] -= 1
                if s[left] in counter_t and window[s[left]] < counter_t[s[left]]:
                    have -= 1
                left += 1
        
        left, right = res
        
        return s[left : right + 1] if resLen != float('inf') else ''