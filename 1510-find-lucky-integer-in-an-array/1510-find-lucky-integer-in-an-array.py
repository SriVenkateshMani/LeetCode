class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count_map = defaultdict(int)
        res = -1
        for i in arr:
            count_map[i] += 1
        
        for key, value in count_map.items():
            if key == value:
                if key > res:
                    res = key
        
        return res
        
        