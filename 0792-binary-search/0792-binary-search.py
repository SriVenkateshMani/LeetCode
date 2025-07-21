class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        u = len(nums) - 1

        while l <= u:
            mp = (l+u) // 2
            if nums[mp] == target:
                return mp
            
            elif nums[mp] < target:
                l = mp + 1
            else:
                u = mp - 1

        return - 1