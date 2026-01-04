class Solution:
    def searchRotatedArray(self, nums, k):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == k:
                return mid

            if nums[start] <= nums[mid]:
                if nums[start] <= k < nums[mid]:
                    end = mid - 1
                else: 
                    start = mid + 1

            else:
                if nums[mid] < k <= nums[end]:
                    start = mid + 1
                else: 
                    end = mid - 1


        return -1

