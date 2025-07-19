class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res_set = set()
        for i in nums:
            res_set.add(i)
        
        return False if len(res_set) == len(nums) else True