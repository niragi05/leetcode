import math
class Solution:
    def countDigit(self, n):
        # Solution 1:
        # count = 0

        # if n == 0:
        #     return 1 

        # while n > 0:
        #     count += 1
        #     n = n // 10

        # return count

        # Solution 2:
        n = abs(n)     

        if n == 0:
            return 1   

        return int(math.log10(n)) + 1

