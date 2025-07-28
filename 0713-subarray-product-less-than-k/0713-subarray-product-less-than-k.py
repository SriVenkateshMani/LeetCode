class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        res = 0
        prod = 1
        n = len(nums)
        while j < n:
            prod *= nums[j]
            
            while prod >= k and i <= j:
                prod //= nums[i]
                i += 1

            res += (j-i+1)
            j += 1
        
        return res
