class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        j = 0
        zero_count = 0
        best = 0
        n = len(nums)

        while j < n:
            if nums[j] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[i] == 0:
                    zero_count -= 1
                i += 1
            
            best = max(best, j-i+1)
            j += 1

        return best

