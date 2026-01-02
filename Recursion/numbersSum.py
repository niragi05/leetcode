class Solution:
    def numbersSum(self, N):
        # Solution 1:
        # sum = 0
        # for i in range (1, N+1):
        #     sum += i

        # return sum
        
        # Solution 2:
        return (N * (N + 1)) // 2