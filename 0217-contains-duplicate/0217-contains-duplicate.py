class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_set = set()

        for i in nums:
            if i in count_set:
                return True
            
            count_set.add(i)
        
        return False