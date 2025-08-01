class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        str_count = defaultdict(int)
        freq_map = defaultdict(int)
        i,j = 0,0
        n = len(s)
        res = 0

        while j < n:
            str_count[s[j]] += 1
            if j - i + 1 > minSize:
                str_count[s[i]] -= 1
                if str_count[s[i]] == 0:
                    del str_count[s[i]]
                i += 1

            if j - i + 1 == minSize:
                if len(str_count) <= maxLetters:
                    sub_str = s[i:j+1]
                    freq_map[sub_str] += 1
                    res = max(res, freq_map[sub_str])
            
            j += 1

        return res
