class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        i, j = 0, 0
        n = len(s)
        res = 0
        
        while j < n:
            freq_map[s[j]] += 1

            while freq_map[s[j]] == k:
                freq_map[s[i]] -= 1
                i += 1
            res += i
            j += 1

        
        return res