class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        children = 0
        cookie = 0
        while children < len(g) and cookie < len(s):
            if s[cookie] >= g[children]:
                children += 1
            cookie += 1
        return children
