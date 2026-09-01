class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_dict = defaultdict(int)

        for i in range(len(s)):
            freq_dict[s[i]] += 1
            freq_dict[t[i]] -= 1

        for i in freq_dict.values():
            if i != 0:
                return False
        
        return True