class Solution:
    def findKthPositive(self, arr, k) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            ## Finding count of missing number at mid
            missing = arr[mid] - (mid + 1)

            if missing >= k:
                high = mid - 1
            else:
                low = mid + 1

        return k + high + 1
        