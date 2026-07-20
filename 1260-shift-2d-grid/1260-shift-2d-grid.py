class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        a = len(grid)
        b = len(grid[0])
        total = a * b
        k %= total
        ans = [[0] * b for _ in range(a)]
        for i in range(a):
            for j in range(b):
                index = i * b + j
                newIndex = (index + k) % total
                c = newIndex // b
                d = newIndex % b
                ans[c][d] = grid[i][j]
        return ans