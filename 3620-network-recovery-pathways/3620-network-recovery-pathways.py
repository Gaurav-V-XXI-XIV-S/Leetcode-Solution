class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        indeg = [0] * n
        mx = 0
        for u, v, w in edges:
            g[u].append((v, w))
            indeg[v] += 1
            mx = max(mx, w)
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        def check(x):
            INF = 10 ** 30
            dist = [INF] * n
            dist[0] = 0
            for u in topo:
                if dist[u] == INF:
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                for v, w in g[u]:
                    if w < x:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
            return dist[n - 1] <= k
        if not check(0):
            return -1
        l, r = 0, mx
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l