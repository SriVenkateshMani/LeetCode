class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i, j = 0,0
        n = len(s)
        res = 0
        vowel_set = {"a", "e", "i", "o", "u"}
        v_count = 0
        while j < n:
            if s[j] in vowel_set:
                v_count += 1
            if j-i+1 == k:
                res = max(res, v_count)
                if s[i] in vowel_set:
                    v_count -= 1
                i += 1
           
            
            j += 1
        
        return res
            
            


