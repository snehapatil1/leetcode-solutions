class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output, line, width = [], [], 0

        for w in words:
            if width + len(w) + len(line) > maxWidth:
                for i in range(maxWidth - width):
                    line[i % (len(line) - 1 or 1)] += " "
                output += ["".join(line)]
                line = []
                width = 0
            
            line += [w]
            width += len(w)
        
        return output + [' '.join(line).ljust(maxWidth)]