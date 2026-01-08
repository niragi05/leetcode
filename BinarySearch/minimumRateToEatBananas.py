import math

class Solution:
    def minimumRateToEatBananas(self, nums, h):
        low = 1
        high = max(nums)

        while low <= high:
            mid = (low + high) // 2

            totalH = 0
            for bananas in nums:
                totalH += math.ceil(bananas / mid)

            if totalH <= h:
                high = mid - 1
                
            else:
                low = mid + 1

        return low

       