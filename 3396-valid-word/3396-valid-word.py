class Solution:
    def isValid(self, word: str) -> bool:
        has_vowel = False
        has_con = False

        if len(word) >= 3:
            for i in word:
                if i.isalpha():
                    if i.lower() in "aeiou":
                        has_vowel = True
                    else:
                        has_con = True
                
                elif not i.isdigit():
                    return False
        
        return has_vowel and has_con




