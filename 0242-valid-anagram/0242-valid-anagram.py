class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in s:
            freq_map[i] += 1
        for i in t:
            if i not in freq_map:
                return False
            freq_map[i] -= 1
            if freq_map[i] == 0:
                del freq_map[i]
        
        return len(freq_map) == 0