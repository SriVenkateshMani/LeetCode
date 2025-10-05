class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        j = 0
        max_val = count = 0
        n = len(nums)

        while j < n:
            if nums[j] == 0:
                count = 0
            else:
                count += 1
            max_val = max(max_val, count)
            j += 1
        
        return max_val