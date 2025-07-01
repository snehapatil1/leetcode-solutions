class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for weight in asteroids:
            while stack and weight < 0 < stack[-1]:
                if abs(weight) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(weight) == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(weight)

        return stack