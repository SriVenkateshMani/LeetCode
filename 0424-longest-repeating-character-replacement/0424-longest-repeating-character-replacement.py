class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        i, j = 0,0
        counts = [0] * 26

        while j < len(s):
            counts[ord(s[j]) - 65] += 1
            while (j-i+1) - max(counts) > k:
                counts[ord(s[i]) - 65] -= 1
                i += 1
            
            longest = max(longest, j-i+1)

            j += 1
        
        return longest
        