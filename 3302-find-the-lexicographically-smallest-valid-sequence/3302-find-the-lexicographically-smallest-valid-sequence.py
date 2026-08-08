class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)
        suf = [-1] * m
        j = n - 1
        for i in range(m - 1, -1, -1):
            while j >= 0 and word1[j] != word2[i]:
                j -= 1
            if j < 0:
                break
            suf[i] = j
            j -= 1
        ans = []
        j = 0
        mismatch_used = False
        for i in range(m):
            while j < n:
                if word1[j] == word2[i]:
                    ans.append(j)
                    j += 1
                    break
                if not mismatch_used:
                    if i == m - 1 or (
                        suf[i + 1] != -1 and suf[i + 1] > j
                    ):
                        ans.append(j)
                        j += 1
                        mismatch_used = True
                        break
                j += 1
            if len(ans) != i + 1:
                return []
        return ans