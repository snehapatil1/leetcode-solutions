class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        
        """
            cur_n = unique songs remaining
            repeated = no of times repeated
            cur_goal = no of songs pending to add
            cur_k = old song can be repeaetd if this is 0
        """
        @lru_cache
        def dp(cur_n, repeated, cur_goal, cur_k):
            # initially cur_k will be k+1 and it will keep on reducing after each selection of song
            # if this becomes 0 then we are free to repeat any old song
            if cur_k == 0:
                repeated += 1
                cur_k = 1
            
            # if no of unique songs remaning to pick > playlist size then that's a wrong combo hence return 0
            if cur_n > cur_goal:
                return 0
            
            # if current playlist size is completed then return 1
            if cur_goal == 0:
                return 1
            
            res = 0
            # Choose new song
            # if any unique song is pending the select new song
            if cur_n > 0:
                # decrement unique songs count by 1, decrement current playlist size by 1, decrement k by 1
                # and call dp to get count for next combo
                res += dp(cur_n - 1, repeated, cur_goal - 1, cur_k - 1) * cur_n
            
            # Choose old song
            # if old song can be repeated now then use old song
            if repeated > 0:
                # since this is an old song do not decrement unique songs count, since old is repeated decrement repeated by 1
                # decrement current playlist size by 1, decrement k by 1
                # and call dp to get count for next combo
                res += dp(cur_n, repeated - 1, cur_goal - 1, cur_k - 1) * repeated
            
            return res
        
        return dp(n, 0, goal, k + 1) % MOD