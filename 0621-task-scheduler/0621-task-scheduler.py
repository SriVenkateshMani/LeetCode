class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = defaultdict(int)
        for t in tasks:
            task_count[t] += 1
        
        max_heap = [-cnt for cnt in task_count.values()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0

        while max_heap or q:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1 
                if count:
                    q.append([count, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
            
        return time

