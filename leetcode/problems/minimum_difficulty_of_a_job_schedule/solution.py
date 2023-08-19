class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n_jobs = len(jobDifficulty)
        
        if n_jobs < d:
            return -1
        
        hardest_job_remaining = [0] * n_jobs
        hardest_job = 0
        for idx in range(n_jobs - 1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[idx])
            hardest_job_remaining[idx] = hardest_job
        
        @lru_cache(None)
        def min_difficulty(job_idx, day):
            if day == d:
                return hardest_job_remaining[job_idx]
            
            hardest = 0
            best = float('inf')

            for idx in range(job_idx, n_jobs - (d - day)):
                hardest = max(hardest, jobDifficulty[idx])
                best = min(best, hardest + min_difficulty(idx + 1, day + 1))
            
            return best
        
        return min_difficulty(0, 1)