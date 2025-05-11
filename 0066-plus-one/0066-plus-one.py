class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = "".join(str(i) for i in digits)
        res = int(res) + 1
        res = str(res)
        res = [int(i) for i in res]
        return res