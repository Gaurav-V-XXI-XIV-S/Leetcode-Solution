class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        class Fenwick:
            def __init__(self, m):
                self.bit = [0] * (m + 1)
            def update(self, i, val):
                while i <= m:
                    self.bit[i] += val
                    i += i & -i
            def query(self, i):
                a = 0
                while i > 0:
                    a += self.bit[i]
                    i -= i & -i
                return a
        pref = [0]
        cur = 0
        for b in nums:
            if b == target:
                cur += 1
            else:
                cur -= 1
            pref.append(cur)
        vals = sorted(set(pref))
        mp = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        bit = Fenwick(m)
        ans = 0
        for c in pref:
            idx = mp[c]
            ans += bit.query(idx - 1)
            bit.update(idx, 1)
        return ans