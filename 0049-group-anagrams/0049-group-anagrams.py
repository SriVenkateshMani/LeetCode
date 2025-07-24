class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_map = defaultdict(list)

        for i in strs:
            sorted_strs = tuple(sorted(i))
            res_map[sorted_strs].append(i) 
        
        return tuple(res_map.values())