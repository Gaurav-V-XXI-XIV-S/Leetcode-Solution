class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        ans = set()

        for i in range(len(s) - 9):
            cur = s[i:i + 10]
            if cur in seen:
                ans.add(cur)
            else:
                seen.add(cur)

        return list(ans)