class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        heap = []

        for i in nums:
            count_dict[i] += 1
        
        for key, val in count_dict.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            
            else:
                heapq.heappushpop(heap, (val, key))
        
        return [i[1] for i in heap]