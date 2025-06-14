class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()
        l = 0
        r = len(nums) - 1

        while l <= r:
            mp = (l+r) // 2
            if nums[mp] == target:
                return mp
            elif nums[mp] < target:
                l = mp + 1
            else:
                r = mp - 1
        
        return -1
