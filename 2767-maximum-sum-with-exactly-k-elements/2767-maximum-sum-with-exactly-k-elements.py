class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        res = 0
        nums = sorted(nums)[::-1]
        for i in range(k):
            res += nums[0]
            nums[0] += 1
        
        return res

