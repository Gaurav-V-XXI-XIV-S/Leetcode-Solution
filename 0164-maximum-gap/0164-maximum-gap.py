class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        mn = min(nums)
        mx = max(nums)
        if mn == mx:
            return 0

        size = max(1, (mx - mn + n - 2) // (n - 1))
        cnt = (mx - mn) // size + 1

        bucket_min = [float("inf")] * cnt
        bucket_max = [float("-inf")] * cnt
        used = [False] * cnt

        for x in nums:
            i = (x - mn) // size
            bucket_min[i] = min(bucket_min[i], x)
            bucket_max[i] = max(bucket_max[i], x)
            used[i] = True

        ans = 0
        prev = mn
        for i in range(cnt):
            if not used[i]:
                continue
            ans = max(ans, bucket_min[i] - prev)
            prev = bucket_max[i]

        return ans