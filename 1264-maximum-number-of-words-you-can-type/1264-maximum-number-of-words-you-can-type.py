class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        broken = set(brokenLetters)
        count = 0

        for word in words:
            if any(ch in broken for ch in word):
                count += 1
        
        return len(words) - count
