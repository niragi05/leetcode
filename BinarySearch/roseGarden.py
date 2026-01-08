class Solution:
    def roseGarden(self, n, nums, k, m):
        if m * k > n:
            return -1

        low, high = min(nums), max(nums)

        while low <= high:
            mid = (low + high) // 2

            count = 0
            bouquet = 0

            for bloom in nums:
                if bloom <= mid:
                    count += 1
                    if count == k:
                        bouquet += 1
                        count = 0
                        if bouquet >= m:
                            break
                else:
                    count = 0

            if bouquet >= m:
                high = mid - 1
            else:
                low = mid + 1

        return low 
     
