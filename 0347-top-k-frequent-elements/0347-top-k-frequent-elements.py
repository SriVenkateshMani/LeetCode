class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        count_map = defaultdict(int)
        for i in nums:
            count_map[i] += 1
        
        for key, val in count_map.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            
            else:
                heapq.heappushpop(heap, (val,key))
        
        return [i[1] for i in heap ]