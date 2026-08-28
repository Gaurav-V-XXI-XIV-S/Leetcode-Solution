class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        odd = 0
        middle = ""
        for i in range(26):
            if freq[i] % 2:
                odd += 1
                middle = chr(i + 97)
        if odd > 1:
            return ""
        half = [x // 2 for x in freq]
        m = n // 2
        remaining = half[:]
        possible = True
        for i in range(m):
            c = ord(target[i]) - 97
            if remaining[c] == 0:
                possible = False
                break
            remaining[c] -= 1
        if possible:
            left = target[:m]
            candidate = left + middle + left[::-1]
            if candidate > target:
                return candidate
        for pos in range(m - 1, -1, -1):
            remaining = half[:]
            possible = True
            for i in range(pos):
                c = ord(target[i]) - 97
                if remaining[c] == 0:
                    possible = False
                    break
                remaining[c] -= 1
            if not possible:
                continue
            current = ord(target[pos]) - 97
            for c in range(current + 1, 26):
                if remaining[c] == 0:
                    continue
                remaining[c] -= 1
                suffix = []
                for x in range(26):
                    suffix.extend(
                        [chr(x + 97)] * remaining[x]
                    )
                left = (
                    target[:pos]
                    + chr(c + 97)
                    + ''.join(suffix)
                )
                candidate = left + middle + left[::-1]
                if candidate > target:
                    return candidate
                remaining[c] += 1
        return ""