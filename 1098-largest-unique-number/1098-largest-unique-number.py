class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num_map = defaultdict(int)
        res = -1
        for i in nums:
            num_map[i] += 1
        
        for key, value in num_map.items():
            if value == 1:
                res = max(res, key)
        
        return res
