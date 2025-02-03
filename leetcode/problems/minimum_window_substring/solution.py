class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countsT = Counter(t)
        window = defaultdict(int)
        left = 0
        output = float('inf')
        have = 0
        need = len(countsT.keys())
        res = [-1, -1]
        resLen = float('inf')

        for right in range(len(s)):
            # increase character count in window
            window[s[right]] = window.get(s[right], 0) + 1
            # if right character is in t string and count of that character is same in both window and t then we have 1 character so increment have by 1
            if s[right] in countsT.keys() and window[s[right]] == countsT[s[right]]:
                have += 1
            
            # if we have every character we need from t then increment left till we get min
            while have == need:
                # if window size is less than current min then consider this as output
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                # reduce character count from window as we will be shifting left
                window[s[left]] -= 1
                # if left character is in t and count of that character in window is less than t then we don't have all characters now so reduce have by 1
                if s[left] in countsT and window[s[left]] < countsT[s[left]]:
                    have -= 1
                # shift left
                left += 1
        
        left, right = res
        return s[left : right + 1] if resLen != float('inf') else ""
