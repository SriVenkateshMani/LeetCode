class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        count_map = defaultdict(int)

        for num in nums:
            count_map[num] += 1

        for key, value in count_map.items():
            if value == 2:
                res.append(key)
        
        return res