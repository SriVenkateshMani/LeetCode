class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)
        i, j = 0,0
        k = len(s1)
        n = len(s2)

        for ch in s1:
            s1_dict[ch] += 1
        
        while j < n:
            s2_dict[s2[j]] += 1

            while j-i+1 > k:
                s2_dict[s2[i]] -= 1
                if s2_dict[s2[i]] == 0:
                    del s2_dict[s2[i]]
                i += 1
            
            if j-i+1 == k and s2_dict == s1_dict:
                return True
            
            j += 1
        
        return False