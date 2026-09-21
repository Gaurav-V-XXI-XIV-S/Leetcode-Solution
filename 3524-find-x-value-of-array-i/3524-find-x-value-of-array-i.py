class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k
        for num in nums:
            rem = num % k
            new_dp = [0] * k
            new_dp[rem] += 1
            for r in range(k):
                if dp[r]:
                    new_dp[(r * rem) % k] += dp[r]
            dp = new_dp
            for r in range(k):
                result[r] += dp[r]
        return result