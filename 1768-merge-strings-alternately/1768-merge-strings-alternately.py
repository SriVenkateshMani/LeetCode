class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        short_arr = min(len(word1), len(word2))

        for i in range(short_arr):
            res += word1[i] + word2[i]
        
        res += word1[short_arr:]
        res += word2[short_arr:]

        return res
