class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        curr_sum = 0
        min_window = float("inf")
        n = len(nums)

        while j < n:
            curr_sum += nums[j]
            while curr_sum >= target:
                min_window = min(min_window, j-i+1)
                curr_sum -= nums[i]
                i += 1
            j += 1
        
        return 0 if min_window == float("inf") else min_window

