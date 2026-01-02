import math
class Solution:
    def divisors(self, n):
        divisor = []

        # for i in range (1, n+1):
        #     if (n % i == 0):
        #         divisor.append(i)

        for i in range (1, math.isqrt(n) + 1):
            if (n % i == 0):
                divisor.append(i)

                if i != n // i:
                    divisor.append(n//i)

        return sorted(divisor)
