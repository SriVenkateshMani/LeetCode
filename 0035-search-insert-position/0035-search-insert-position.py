class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mp = (l + r) // 2
            if nums[mp] == target:
                return mp
            if target < nums[mp]:
                r = mp - 1
            else:
                l = mp + 1
        return l
