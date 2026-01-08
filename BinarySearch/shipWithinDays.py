class Solution:
    def shipWithinDays(self, weights, days):
        # Your code goes here

        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2

            capacity = 0
            day = 1

            for w in weights:
                if capacity + w > mid:
                    day += 1
                    capacity = w
                    
                else:
                    capacity += w

            if day <= days:
                high = mid - 1

            else:
                low = mid + 1

        return low