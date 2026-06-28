class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def dfs(i, path):
            if len(path) == 4:
                if i == len(s):
                    ans.append(".".join(path))
                return
            for j in range(1, 4):
                if i + j > len(s):
                    break
                part = s[i:i + j]
                if (part[0] == "0" and len(part) > 1) or int(part) > 255:
                    continue
                dfs(i + j, path + [part])

        dfs(0, [])
        return ans