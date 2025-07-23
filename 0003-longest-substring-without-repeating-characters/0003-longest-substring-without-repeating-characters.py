class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        storedset = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in storedset:
                storedset.remove(s[l])
                l += 1
            storedset.add(s[r])
            res = max(res, r-l+1)
        
        return res