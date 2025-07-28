class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        used = [0] * (n+1)
        level = [0] * (n+1)
        G = [[] for _ in range(n+1)]

        for u, v in edges:
            G[u].append(v)
            G[v].append(u)

        q = deque()
        q.append(source)
        used[source] = 1

        while q:
            removed = q.popleft()

            for u in G[removed]:
                if not used[u]:
                    if u == destination:
                        return True
                    q.append(u)
                    used[u] = 1
        
        return False