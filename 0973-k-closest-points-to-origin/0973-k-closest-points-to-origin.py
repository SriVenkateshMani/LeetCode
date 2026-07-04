class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for p in points:
            dist = (((p[0] - 0) ** 2 + (p[1] - 0) ** 2)) ** 0.5
            if len(res) < k:
                heapq.heappush(res, (-dist, p))
            else:
                heapq.heappushpop(res, (-dist, p))
        
        return [i[1] for i in res]