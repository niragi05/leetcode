class Solution:
    def GCD(self, n1, n2):
        ## Solution 1
        # gcd = 1

        # for i in range (1, min(n1, n2) + 1):
        #     if (n1 % i == 0 and n2 % i == 0):
        #         gcd = i

        ## Solution 2
        # gcd = 1
        
        # for i in range (min(n1, n2), 0, -1):
        #     if (n1 % i == 0 and n2 % i == 0):
        #         return i
        
        # return gcd

        ## Solution 3

        while n1 > 0 and n2 > 0:
            if n1 > n2:
                n1 = n1 % n2
            else:
                n2 = n2 % n1

        if n1 == 0:
            return n2

        return n1 
