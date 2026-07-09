from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        cnt = [0] * (n + 1)
        sm = [0] * (n + 1)
        val = [0] * (n + 1)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        for i, ch in enumerate(s):
            d = int(ch)
            cnt[i + 1] = cnt[i]
            sm[i + 1] = sm[i]
            val[i + 1] = val[i]

            if d != 0:
                cnt[i + 1] += 1
                sm[i + 1] += d
                val[i + 1] = (val[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:
            k = cnt[r + 1] - cnt[l]
            digit_sum = sm[r + 1] - sm[l]
            x = (val[r + 1] - val[l] * pow10[k]) % MOD
            ans.append((x * digit_sum) % MOD)

        return ans