class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # n(logn)
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False