class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l, r = 0, 0
        hash_map = defaultdict(int)
        res = 0

        while r < len(s):
            hash_map[s[r]] += 1

            if len(hash_map) <= 2:
                res = max(res, r-l+1)

            while len(hash_map) > 2 and l <= r:
                hash_map[s[l]] -= 1
                if hash_map[s[l]] == 0:
                    del hash_map[s[l]]
                l += 1
            
            r += 1
        
        return res

