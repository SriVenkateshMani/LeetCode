class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        i, j = 0, 0 
        res = 0
        n = len(s)
        count_map = defaultdict(int)

        while j < n:
            count_map[s[j]] += 1
            if len(count_map) <= 2:
                res = max(res, j-i+1)

            while len(count_map) > 2 and i <= j:
                count_map[s[i]] -= 1
                if count_map[s[i]] == 0:
                    del count_map[s[i]]
                i += 1
            j += 1
        
        return res



