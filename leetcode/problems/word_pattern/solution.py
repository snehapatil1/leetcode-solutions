class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = defaultdict(str)
        words = s.split()
        if len(words) != len(pattern):
            return False
        if len(set(words)) != len(set(pattern)):
            return False

        for idx, word in enumerate(words):
            if pattern[idx] not in pattern_map:
                pattern_map[pattern[idx]] = word
                continue
            if pattern[idx] in pattern_map and pattern_map[pattern[idx]] != word:
                return False
        
        return True

