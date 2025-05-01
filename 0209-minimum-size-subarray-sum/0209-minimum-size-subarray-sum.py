class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cur_sum = 0
        length = float("inf")

        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                length = min(length, r-l+1)
                cur_sum -= nums[l]
                l += 1

        return 0 if length == float("inf") else length