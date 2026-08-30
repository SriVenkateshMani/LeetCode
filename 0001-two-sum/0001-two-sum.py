class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = defaultdict(int)

        for i, val in enumerate(nums):
            if (target - val) in idx_map:
                return [idx_map[target - val], i]
            
            idx_map[val] += i
        
            