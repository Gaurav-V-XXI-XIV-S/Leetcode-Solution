class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        n = len(s)
        prefix = []
        for i in range(n):
            t = ord(target[i]) - ord('a')
            if freq[t] > 0:
                freq[t] -= 1
                prefix.append(target[i])
                continue
            for c in range(t + 1, 26):
                if freq[c] > 0:
                    freq[c] -= 1
                    result = ''.join(prefix)
                    result += chr(c + ord('a'))
                    for x in range(26):
                        result += chr(x + ord('a')) * freq[x]
                    return result
            break
        while prefix:
            last_char = prefix.pop()
            last = ord(last_char) - ord('a')
            freq[last] += 1
            for c in range(last + 1, 26):
                if freq[c] > 0:
                    freq[c] -= 1
                    result = ''.join(prefix)
                    result += chr(c + ord('a'))
                    for x in range(26):
                        result += chr(x + ord('a')) * freq[x]
                    return result
        return ""