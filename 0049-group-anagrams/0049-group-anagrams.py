class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for str in strs:
            sorted_str = tuple(sorted(str))
            mapping[sorted_str].append(str)
        
        return list(mapping.values())
