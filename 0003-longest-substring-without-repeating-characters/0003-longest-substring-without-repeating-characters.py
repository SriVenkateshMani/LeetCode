class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        n = len(s)
        res = 0
        hash_map = defaultdict(int)

        while j < n:
            hash_map[s[j]] += 1
            while hash_map[s[j]] > 1:
                hash_map[s[i]] -= 1
                i += 1
            res = max(res, j-i+1)
            j += 1
        
        return res