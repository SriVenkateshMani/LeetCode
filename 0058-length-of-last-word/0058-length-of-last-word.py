class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1, -1, -1):
            if res == 0 and s[i] == " ":
                continue
            elif res != 0 and s[i] == " ":
                break
            else:
                res += 1
        return res
            