class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        heap = []

        for i in nums:
            count_map[i] += 1
        
        for key, val in count_map.items():
            if len(heap) < k:
                heappush(heap, (val, key))
            
            else:
                heappushpop(heap, (val, key))
        
        return [h[1] for h in heap]
