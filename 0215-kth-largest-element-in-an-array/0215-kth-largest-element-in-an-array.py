class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = -nums[i]

        heapq.heapify(nums)
        res = []
        for i in range(k):
            largest = -heapq.heappop(nums)
            res.append(largest)

        return res[-1]
