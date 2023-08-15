class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = [0]
        longest_path_value = 0
        input_list = input.split('\n')

        for path in input_list:
            words = path.split('\t')
            depth, name = len(words) - 1, words[-1]
            while len(stack) > depth + 1:
                stack.pop()
            if '.' in name:
                # it is a file
                longest_path_value = max(longest_path_value, stack[-1] + len(name))
            else:
                # it is a path
                stack.append(stack[-1] + len(name) + 1)
                
        return longest_path_value