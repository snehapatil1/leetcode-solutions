class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1

        while left < len(s) and s[left] == " ":
            left += 1
        
        while right >= 0 and s[right] == " ":
            right -= 1
        
        queue, word = deque(), []

        while left <= right:
            if s[left] == " " and word:
                queue.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        queue.appendleft("".join(word))

        return " ".join(queue)