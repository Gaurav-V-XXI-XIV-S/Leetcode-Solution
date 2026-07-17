class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        mx = max(nums)

        # frequency
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # pairs divisible by d
        pair_div = [0] * (mx + 1)

        for d in range(1, mx + 1):
            cnt = 0
            for multiple in range(d, mx + 1, d):
                cnt += freq[multiple]
            pair_div[d] = cnt * (cnt - 1) // 2

        # exact gcd count
        exact = [0] * (mx + 1)

        for d in range(mx, 0, -1):
            exact[d] = pair_div[d]
            for multiple in range(2 * d, mx + 1, d):
                exact[d] -= exact[multiple]

        # prefix frequencies
        values = []
        prefix = []

        cur = 0
        for g in range(1, mx + 1):
            if exact[g]:
                cur += exact[g]
                values.append(g)
                prefix.append(cur)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans