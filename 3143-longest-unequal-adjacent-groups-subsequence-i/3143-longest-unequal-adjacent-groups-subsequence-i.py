class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        res.append(words[0])
        for i in range(1,len(groups)):
            if groups[i-1] != groups[i]:
                res.append(words[i])
        
        return res

            
            