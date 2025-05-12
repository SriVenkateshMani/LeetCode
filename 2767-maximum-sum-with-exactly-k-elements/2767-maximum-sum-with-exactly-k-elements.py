class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        res = 0
        max_num = max(nums)
        for i in range(k):
            res += max_num
            max_num += 1
        return res

