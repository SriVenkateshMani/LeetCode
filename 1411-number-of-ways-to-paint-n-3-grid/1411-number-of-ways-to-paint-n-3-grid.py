class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        aba, abc = 6, 6

        for i in range(2, n+1):
            new_aba = (3 * aba + 2 * abc) % mod
            new_abc = (2 * aba + 2 * abc) % mod
            aba, abc = new_aba, new_abc
        
        return (aba + abc) % mod