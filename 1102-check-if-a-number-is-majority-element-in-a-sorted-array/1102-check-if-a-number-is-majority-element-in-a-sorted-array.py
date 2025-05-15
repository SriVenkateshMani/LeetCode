class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        res = 0
        for i in nums:
            if i == target:
                res += 1
        if len(nums) / 2 >= res:
            return False
        elif len(nums) / 2 < res:
            return True