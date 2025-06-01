class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        l, r = 0, 0
        o, c = 0, 0

        while r < len(s):
            if s[r] == "(":
                o += 1
            else:
                c += 1
            
            if o == c and o != 0:
                stack.append(s[l+1 : r])
                l = r + 1
            r += 1
        
        return "".join(stack)