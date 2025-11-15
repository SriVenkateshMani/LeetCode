class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        i, j = 0, 0
        n = len(s)
        res = 0
        
        while j < n:
            freq_map[s[j]] += 1

            while freq_map[s[j]] >= k:
                res += (n-j)
                freq_map[s[i]] -= 1
                if freq_map[s[i]] == 0:
                    del freq_map[s[i]]
                i += 1
            j += 1

        
        return res