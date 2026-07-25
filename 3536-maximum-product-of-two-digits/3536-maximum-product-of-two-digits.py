class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        while n:
            digits.append(n % 10)
            n //= 10
        value = 0
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                sum = digits[i] * digits[j]
                if sum > value:
                    value = sum
        return value