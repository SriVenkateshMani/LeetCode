from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_map = defaultdict(list)
        for i in strs:
            sorted_s = tuple(i)
            count_map[sorted_s].append(i)
        
        return list(count_map.values())



        