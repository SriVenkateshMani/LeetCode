class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        normal_res = 0
        first_last_diff = abs(nums[0] - nums[-1])
        for i in range(1, len(nums)):
            normal_res = max(normal_res, abs(nums[i] - nums[i-1]))

        return max(normal_res, first_last_diff)