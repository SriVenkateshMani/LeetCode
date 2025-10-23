class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(i) for i in s]

        while len(s) > 2:
            for i in range(len(s)-1):
                s[i] = (s[i] + s[i+1]) % 10
            s.pop()

        if s[0] == s[1]:
            return True
        else:
            return False
