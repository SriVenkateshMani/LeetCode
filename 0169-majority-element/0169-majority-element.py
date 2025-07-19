class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = defaultdict(int)
        max_val = 0
        for i in nums:
            count_map[i] += 1
        
        for key, value in count_map.items():
            max_val = max(max_val, value)
            if count_map[key] == max_val:
                res = key
        
        return res
            
    