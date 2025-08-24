class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        i, j = 0, 0
        res = 0
        n = len(nums)

        while j < n:
            if nums[j] == 0:
                zero_count += 1
            if zero_count == 0:
                res = max(res, j-i+1)
            elif zero_count == 1:
                res = max(res, j-i)
            
            
            while zero_count > 1 and i < j:
                if nums[i] == 0:
                    zero_count -= 1

                i += 1
                res = max(res, j-i)
            

            j += 1

        return res-1 if zero_count == 0 else res
        