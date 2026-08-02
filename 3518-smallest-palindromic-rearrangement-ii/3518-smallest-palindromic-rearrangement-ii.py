class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = 10**6 + 1

        cnt = Counter(s)
        half = Counter()
        mid = ""

        for ch, f in cnt.items():
            half[ch] = f // 2
            if f % 2:
                mid = ch

        def count(freq):
            rem = sum(freq.values())
            ans = 1
            for v in freq.values():
                if v:
                    ans *= comb(rem, v)
                    if ans > LIMIT:
                        return LIMIT
                    rem -= v
            return ans

        if count(half) < k:
            return ""

        left = []
        total = sum(half.values())

        while total:
            for ch in sorted(half):
                if half[ch] == 0:
                    continue

                half[ch] -= 1
                ways = count(half)

                if ways >= k:
                    left.append(ch)
                    total -= 1
                    break

                k -= ways
                half[ch] += 1

        left = "".join(left)
        return left + mid + left[::-1]