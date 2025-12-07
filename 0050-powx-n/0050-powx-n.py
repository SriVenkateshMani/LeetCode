class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        temp = n
        n=abs(n)
        while n > 0:
            if n % 2 == 1:
                res *= x
                n -= 1
            else:
                x *= x
                n //= 2

        if temp < 0:
            return 1 / res
        
        return res