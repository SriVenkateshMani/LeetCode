class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []

        for num in nums:
            if len(res) < k:
                heapq.heappush(res, num)
            else:
                heapq.heappushpop(res, num)
        
        return res[0]