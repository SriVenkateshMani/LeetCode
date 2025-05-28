class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        result = []
    
        for word in words:
            word_set = set(word.lower())
            if word_set <= first or word_set <= second or word_set <= third:
                result.append(word)
        
        return result