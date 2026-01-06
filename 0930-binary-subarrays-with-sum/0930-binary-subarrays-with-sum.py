class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def atmost(k):
            if k < 0:
                return 0
            
            cur_sum = 0
            res = 0
            i, j = 0, 0
            n = len(nums)

            while j < n:
                cur_sum += nums[j]

                while cur_sum > k:
                    cur_sum -= nums[i] 
                    i += 1
                
                res += j-i+1
                j += 1
            
            return res
        
        return atmost(goal) - atmost(goal-1)