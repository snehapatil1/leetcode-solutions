class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # ========== Using Prefix Sum ==========
        n = len(customers)

        if n == 1:
            return 0
        
        left_N_sum, right_N_sum = [0] * (n + 1), [0] * (n + 1)
        total_penalty = []

        for idx in range(n + 1):
            if customers[idx - 1] == 'N':
                left_N_sum[idx] = left_N_sum[idx - 1] + 1
            else:
                left_N_sum[idx] = left_N_sum[idx - 1]
        
        for idx in range(n - 1, -1, -1):
            if customers[idx] == 'Y':
                right_N_sum[idx] = right_N_sum[idx + 1] + 1
            else:
                right_N_sum[idx] = right_N_sum[idx + 1]
        
        for idx in range(n + 1):
            heapq.heappush(total_penalty, (left_N_sum[idx] + right_N_sum[idx], idx))
        
        return heapq.heappop(total_penalty)[1]

        # ========== Using One Iteration ==========
        # min_penalty, curr_penalty = 0, 0
        # earliest_hour = 0

        # for idx, ch in enumerate(customers):
        #     if ch == 'Y':
        #         curr_penalty -= 1
        #     else:
        #         curr_penalty += 1
            
        #     if curr_penalty < min_penalty:
        #         earliest_hour = idx + 1
        #         min_penalty = curr_penalty
        
        # return earliest_hour