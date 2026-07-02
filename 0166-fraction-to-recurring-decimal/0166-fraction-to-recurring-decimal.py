class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        ans = []

        if (numerator < 0) ^ (denominator < 0):
            ans.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        ans.append(str(numerator // denominator))
        rem = numerator % denominator

        if rem == 0:
            return "".join(ans)

        ans.append(".")
        pos = {}

        while rem:
            if rem in pos:
                ans.insert(pos[rem], "(")
                ans.append(")")
                break

            pos[rem] = len(ans)
            rem *= 10
            ans.append(str(rem // denominator))
            rem %= denominator

        return "".join(ans)
        