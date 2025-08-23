class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        cur_sum = 0
        min_len = float('inf')
        n = len(nums)
        while j < n:
            cur_sum += nums[j]
            while cur_sum >= target:
                min_len = min(min_len, j-i+1)
                cur_sum -= nums[i]
                i += 1
            j += 1
        return 0 if min_len == float('inf') else min_len
                


