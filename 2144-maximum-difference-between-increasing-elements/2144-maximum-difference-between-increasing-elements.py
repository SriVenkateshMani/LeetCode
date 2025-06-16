class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num = nums[0]
        max_diff = 0
        for i in range(1, len(nums)):
            if nums[i] > min_num:
                max_diff = max(max_diff, nums[i]-min_num)
            else:
                min_num = nums[i]
        return -1 if max_diff == 0 else max_diff
