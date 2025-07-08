class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        hmap = Counter(p)
        s_count = Counter()
        l, r, n = 0, len(p), len(s)
        if n < r:
            return []

        for i in range(n):
            s_count[s[i]] += 1
            if i >= r:
                if s_count[s[i - r]] == 1:
                    del s_count[s[i - r]]
                else:
                    s_count[s[i - r]] -= 1
            if s_count == hmap:
                output.append(i - r + 1)

        return output