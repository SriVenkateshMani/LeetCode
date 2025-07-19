class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res_set = set()
        for i in nums:
            res_set.add(i)
        
        return len(res_set) != len(nums) 