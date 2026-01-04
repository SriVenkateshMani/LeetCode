class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(m)]
        k = len(original)

        if m * n != k:
            return []

        for i in range(k):
            res[i // n][i % n] = original[i]
        
        return res