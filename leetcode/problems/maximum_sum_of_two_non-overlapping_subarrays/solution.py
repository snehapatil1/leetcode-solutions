class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        max_subarray_M = collections.deque([0])
        max_subarray_L = collections.deque([0])
        sum_L = 0
        sum_M = 0
        maximum_combined_sum = 0
        
        A = nums
        L = firstLen
        M = secondLen
        for i in range(len(A) - 1, -1, -1):
            sum_L += A[i]
            sum_M += A[i]
            max_subarray_M.appendleft(max(sum_M, max_subarray_M[0]))
            max_subarray_L.appendleft(max(sum_L, max_subarray_L[0]))
                 
            if i + M + L <= len(A):
                maximum_combined_sum = max(maximum_combined_sum, sum_M + max_subarray_L[-1], sum_L + max_subarray_M[-1])
     
            if len(max_subarray_L) == M + 1 :
                max_subarray_L.pop()
  
            if len(max_subarray_M) == L + 1 :
                max_subarray_M.pop()              
                
            if i + L <= len(A):
                sum_L -= A[i + L - 1]
                              
            if i + M <= len(A):
                sum_M -= A[i + M - 1]
                
        return maximum_combined_sum