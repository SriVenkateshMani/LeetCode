class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_map = defaultdict(int)
        res = 0

        for i in s:
            count_map[i] += 1
            if count_map[i] % 2 == 0:
                res += 2
        
        for value in count_map.values():
            if value % 2 == 1:
                res += 1
                break
        
        return res
        