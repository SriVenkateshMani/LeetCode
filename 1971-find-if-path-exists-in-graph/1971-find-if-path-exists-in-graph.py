class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        graph = defaultdict(list)
        q = deque([source])
        visited = set([source])

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        

        while q:
            node = q.popleft()

            if node == destination:
                return True
            
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    q.append(n)
        
        return False