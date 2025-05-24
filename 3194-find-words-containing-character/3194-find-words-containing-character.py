class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] == x:
                    res.append(i)
                    break
        
        return res
