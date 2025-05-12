class Solution:
    def balancedStringSplit(self, s: str) -> int:
        var_track = 0
        res = 0
        for i in s:
            if i == 'R':
                var_track += 1
            else:
                var_track -= 1
            
            if var_track == 0:
                res += 1
        return res
