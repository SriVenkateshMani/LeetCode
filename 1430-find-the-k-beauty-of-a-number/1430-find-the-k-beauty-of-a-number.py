class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        res = 0

        for i in range(len(num)-k+1):
            var = int(num[i:i+k])
            if var != 0 and int(num) % var == 0:
                res += 1
        
        return res

