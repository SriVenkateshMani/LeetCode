class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for i , ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')' and stack:
                stack.pop()
            elif ch == ')' and not stack:
                s[i] = ''
        
        for i in stack:
            s[i] = ''
        return ''.join(s)
