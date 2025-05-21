class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_val = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                max_val = max(max_val,count)
                count = 0
        return max(max_val, count)

