class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in s:
            if stack and stack[-1] == "(" and i == ")":
                stack.pop()
            elif stack and stack[-1] == i == ")":
                stack.append(i)
            elif stack and stack[-1] == i == "(":
                stack.append(i)
            elif stack and stack[-1] == ")" and i == "(":
                stack.append(i)
            elif not stack:
                stack.append(i)
        
        return len(stack)