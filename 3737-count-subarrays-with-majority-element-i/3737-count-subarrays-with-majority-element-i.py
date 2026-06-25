class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pref = [0]
        cur = 0
        for x in nums:
            cur += 1 if x == target else -1
            pref.append(cur)
        ans = 0
        for j in range(1, n + 1):
            for i in range(j):
                if pref[i] < pref[j]:
                    ans += 1
        return ans