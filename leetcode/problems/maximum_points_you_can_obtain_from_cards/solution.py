class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # =============== Backtracking Approach (but fails for large input array due to memory limit exceeded) ===============
        # left, right = 0, len(cardPoints) - 1
        # if k == len(cardPoints):
        #     return sum(cardPoints)
        
        # @lru_cache(None)
        # def backtrack(left, right, max_score, turns_left):
        #     if not turns_left or left == len(cardPoints) or right == 0:
        #         return max_score
            
        #     return max(backtrack(left + 1, right, max_score + cardPoints[left], turns_left - 1), backtrack(left, right - 1, max_score + cardPoints[right], turns_left - 1))
        
        # return backtrack(left, right, 0, k)

        # =============== DP Approach (takes 80s for large input array) ===============
        # n = len(cardPoints)
        # dp = [0] * (k + 1)
        # for i in range(n - k, n):
        #     dp[0] += cardPoints[i]
        
        # max_score = dp[0]
        
        # for i in range(1, k + 1):
        #     dp[i] = dp[i - 1] - cardPoints[n - k + i - 1] + cardPoints[i - 1]
        #     max_score = max(max_score, dp[i])
        
        # return max_score

        # =============== Sliding Window Approach (takes 62s for large input array) [OPTIMAL SOLUTION] ===============
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        
        # if number of cards is equal to array size then return full sum
        if k == n:
            return total_sum
        
        # if only one card then return max of first and last element from array
        if k == 1:
            return max(cardPoints[0], cardPoints[n - 1])
        
        window_size = n - k

        # if window size is 1 then remove min element from array and return remaining sum
        if window_size == 1:
            return total_sum - min(cardPoints)

        window_sum = sum(cardPoints[:window_size])
        max_score = total_sum - window_sum

        for i in range(1, n - window_size + 1):
            window_sum += cardPoints[i + window_size - 1] - cardPoints[i - 1]
            max_score = max(max_score, total_sum - window_sum)
        
        return max_score