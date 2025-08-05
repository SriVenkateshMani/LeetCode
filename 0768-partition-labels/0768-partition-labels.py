class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index_map = defaultdict(int)
        res = []
        size = end = 0

        for i, n in enumerate(s):
            last_index_map[n] = i
        
        for i, n in enumerate(s):
            size += 1
            end = max(end, last_index_map[n])

            if i == end:
                res.append(size)
                size = 0
        
        return res
