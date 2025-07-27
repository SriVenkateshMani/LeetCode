class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count_map = defaultdict(int)

        i, j = 0, 0 
        res = 0

        while j < len(s):
            count_map[s[j]] += 1

            while (i <= j and len(count_map) >= 3):
                res += len(s)-j
                count_map[s[i]] -= 1
                if count_map[s[i]] == 0:
                    del count_map[s[i]]
                i += 1
            
            j += 1
        
        return res