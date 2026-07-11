class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num):
            x = num
            while x > 0:
                digit = x % 10
                if digit == 0 or num % digit != 0:
                    return False
                x //= 10
            return True
        ans = []
        for num in range(left, right + 1):
            if isSelfDividing(num):
                ans.append(num)
        return ans