class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        n = len(s)
        k = len(t)
        i,j = 0,0
        res = ""
        min_size = float("inf")

        if len(s) < len(t):
            return res
     
        for ch in t:
            t_dict[ch] += 1
        
        while j < n:
            s_dict[s[j]] += 1

            while all(s_dict[ch] >= t_dict[ch] for ch in t_dict):
                if j-i+1 < min_size:
                    min_size = j-i+1
                    res = s[i:j+1]

                s_dict[s[i]] -= 1
                if s_dict[s[i]] == 0:
                    del s_dict[s[i]]
                i += 1
            
            j += 1
        
        return res

