class Solution:
    def isPrime(self, n):
        # Solution 1:
        if n == 1:
            return False
            
        for i in range(2, n+1):
            if n % i == 0 and i != n:
                return False
        return True
            