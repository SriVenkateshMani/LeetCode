class Solution:
    def maxDistinct(self, s: str) -> int:
        freq_map = defaultdict(int)

        for i in s:
            freq_map[i] += 1
    
        return len(freq_map)