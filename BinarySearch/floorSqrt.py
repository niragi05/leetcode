class Solution:
    def floorSqrt(self, n: int) -> int:
        #  Brute Force
        # ans = 0

        # for i in range(1, n + 1):
        #     if i * i <= n:
        #         ans = i
        #     else:
        #         break
        # return ans

        # Optimal Solution

        if n < 2:
            return n

        left, right, ans = 1, n // 2, 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
