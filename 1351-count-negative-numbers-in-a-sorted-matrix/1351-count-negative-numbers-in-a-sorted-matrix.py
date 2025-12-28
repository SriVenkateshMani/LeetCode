class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0

        for g in grid:
            n = len(g)

            if g[0] < 0:
                res += n
                continue

            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if g[mid] < 0:
                    r = mid - 1
                else:          # g[mid] >= 0
                    l = mid + 1

            # l is now the index of the first negative
            res += n - l

        return res
