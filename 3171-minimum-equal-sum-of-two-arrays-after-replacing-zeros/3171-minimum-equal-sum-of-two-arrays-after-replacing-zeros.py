class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        zero_1 = 0
        zero_2 = 0

        for i in nums1:
            sum1 += i
            if i == 0:
                sum1 += 1
                zero_1 += 1
        
        for i in nums2:
            sum2 += i
            if i == 0:
                sum2 += 1
                zero_2 += 1
        if (sum1 > sum2 and zero_2 == 0) or (sum2 > sum1 and zero_1 == 0):
            return -1
        return max(sum1, sum2)