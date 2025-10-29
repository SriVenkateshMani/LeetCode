class Solution:
    def smallestNumber(self, n: int) -> int:
        v = 0
        while v <= n:
            k = (2 ** v) - 1
            if k >= n:
                return k
            v += 1