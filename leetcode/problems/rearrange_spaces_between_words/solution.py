class Solution:
    def reorderSpaces(self, text: str) -> str:
        original_length = len(text)
        words = text.split()
        spaces = text.count(" ")
        text.strip()

        if len(words) == 1:
            return words[0] + " "*spaces

        ideal_spaces = spaces // (len(words) - 1)
        remaining_spaces = spaces - (len(words) - 1) * ideal_spaces

        return (" "*ideal_spaces).join(words) + " "*remaining_spaces