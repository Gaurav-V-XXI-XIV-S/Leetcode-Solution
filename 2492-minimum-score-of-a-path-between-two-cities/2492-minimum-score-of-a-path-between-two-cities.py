class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
        vis = set()
        ans = float('inf')
        def dfs(u):
            nonlocal ans
            vis.add(u)
            for v, d in graph[u]:
                ans = min(ans, d)
                if v not in vis:
                    dfs(v)
        dfs(1)
        return ans