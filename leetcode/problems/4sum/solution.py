class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        is_satisfied = self.areConstraintsSatisfied(nums, target)
        if (not is_satisfied):
            return False
        
        nums.sort()
        n = len(nums)
        ans = []
        
        i = 0
        while i<n:
            j=i+1
            while j<n:
                end=n-1
                strt=j+1
                nTarget=target-nums[i]-nums[j]
                
                while strt<end:                    
                    if nums[strt]+nums[end]==nTarget:
                        ans.append([nums[i],nums[j],nums[strt],nums[end]])

                        third=nums[strt]
                        fourth=nums[end]
                        while strt<end and nums[strt]==third:
                            strt+=1
                        while strt<end and nums[end]==fourth:
                            end-=1
                    elif nums[strt]+nums[end]>nTarget:
                        end-=1
                    else:
                        strt+=1
                t=nums[j]
                while j<n and nums[j]==t:
                    j+=1
            t2=nums[i]
            while i<n and nums[i]==t2:
                i+=1
        return ans
    
    def areConstraintsSatisfied(self, nums, target):
        if (len(nums) < 1) or (len(nums) > 200):
            return False
        
        for ele in nums:
            if (ele < -10**9) or (ele > 10**9):
                return False
        
        if (target < -10**9) or (target > 10**9):
            return False
        
        return True