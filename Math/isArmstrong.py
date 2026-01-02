import math

class Solution:
    def isArmstrong(self, n):
        count = len(str(n))
        rem = n
        
        sum = 0

        while rem > 0:
            last = rem % 10
            rem = rem // 10
            sum += last ** count

        return sum == n
