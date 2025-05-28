class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, len(nums) - 1)

    def helper(self, nums: List[int], target: int, L: int, R: int) -> int:
        if L > R:
            return -1
        
        m = (L + R) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.helper(nums, target, m + 1, R)
        else:
            return self.helper(nums, target, L, m - 1)