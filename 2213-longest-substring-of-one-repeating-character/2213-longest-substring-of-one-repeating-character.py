class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)

        lc = [''] * (4 * n)
        rc = [''] * (4 * n)
        lp = [0] * (4 * n)
        rp = [0] * (4 * n)
        mx = [0] * (4 * n)
        length = [0] * (4 * n)

        def merge(v):
            a = v * 2
            b = v * 2 + 1

            lc[v] = lc[a]
            rc[v] = rc[b]
            length[v] = length[a] + length[b]

            lp[v] = lp[a]
            rp[v] = rp[b]
            mx[v] = max(mx[a], mx[b])

            if rc[a] == lc[b]:
                if lp[a] == length[a]:
                    lp[v] = length[a] + lp[b]

                if rp[b] == length[b]:
                    rp[v] = length[b] + rp[a]

                mx[v] = max(mx[v], rp[a] + lp[b])

        def build(v, l, r):
            length[v] = r - l + 1

            if l == r:
                lc[v] = rc[v] = s[l]
                lp[v] = rp[v] = mx[v] = 1
                return

            mid = (l + r) // 2
            build(v * 2, l, mid)
            build(v * 2 + 1, mid + 1, r)
            merge(v)

        def update(v, l, r, idx, ch):
            if l == r:
                lc[v] = rc[v] = ch
                lp[v] = rp[v] = mx[v] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(v * 2, l, mid, idx, ch)
            else:
                update(v * 2 + 1, mid + 1, r, idx, ch)

            merge(v)

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(mx[1])

        return ans