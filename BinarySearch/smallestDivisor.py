import math
class Solution:
    def smallestDivisor(self, nums, limit):
        low, high = 1, max(nums)

        while low <= high:
            mid = (low + high) // 2

            total = 0
            for num in nums:
                total += math.ceil(num / mid)

            if total <= limit:
                high = mid - 1
            else:
                low = mid + 1

        return low

            
       