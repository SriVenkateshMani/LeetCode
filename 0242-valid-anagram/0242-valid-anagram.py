class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        freq_dict = defaultdict(int)

        for c in s:
            freq_dict[c] += 1
        
        for c in t:
            if c in freq_dict:
                freq_dict[c] -= 1

        for i in freq_dict.values():
            if i != 0:
                return False
        
        return True