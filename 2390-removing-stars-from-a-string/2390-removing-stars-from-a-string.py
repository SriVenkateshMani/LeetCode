class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isalpha():
                stack.append(i)
            elif i == "*":
                stack.pop()
        
        return "".join(stack)