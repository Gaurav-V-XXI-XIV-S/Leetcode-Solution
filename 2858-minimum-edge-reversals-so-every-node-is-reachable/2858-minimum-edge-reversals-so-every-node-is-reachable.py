class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append((v, 0))
            graph[v].append((u, 1))
        ans = [0] * n
        def dfs1(node, parent):
            total = 0
            for nei, cost in graph[node]:
                if nei != parent:
                    total += cost + dfs1(nei, node)
            return total
        ans[0] = dfs1(0, -1)
        def dfs2(node, parent):
            for nei, cost in graph[node]:
                if nei == parent:
                    continue
                if cost == 0:
                    ans[nei] = ans[node] + 1
                else:
                    ans[nei] = ans[node] - 1
                dfs2(nei, node)
        dfs2(0, -1)
        return ans