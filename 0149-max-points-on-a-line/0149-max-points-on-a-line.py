class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n <= 2:
            return n

        answer = 0

        for i in range(n):
            count = defaultdict(int)

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                g = gcd(dx, dy)
                dx //= g
                dy //= g

                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                count[(dx, dy)] += 1

            max_line = 0
            for value in count.values():
                max_line = max(max_line, value)

            answer = max(answer, max_line + 1)

        return answer