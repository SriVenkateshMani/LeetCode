class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(nums, k):
            res = 0
            i,j = 0,0
            n = len(nums)

            while j < n:
                if nums[j] % 2 == 1:
                    k -= 1
                while k < 0:
                    if nums[i] % 2 == 1:
                        k += 1
                    i += 1
                res += j - i + 1
                
                
                j += 1
            return res
        
        return atmost(nums, k) - atmost(nums, k-1)
            
