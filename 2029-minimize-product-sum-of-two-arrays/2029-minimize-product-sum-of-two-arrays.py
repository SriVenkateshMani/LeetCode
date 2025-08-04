class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        nums2 = nums2[::-1]
        total = 0
        for i, j in zip(nums1, nums2):
            curr_prod = i*j
            total += curr_prod
        
        return total