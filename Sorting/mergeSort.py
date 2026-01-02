class Solution:
    def mergeSort(self, nums):
        n = len(nums)

        if n <= 1:
            return nums

        temp = [0] * n

        def sort(lo, hi):
            if hi - lo <= 1:
                return
            
            mid = (lo + hi) // 2
            sort(lo, mid)
            sort(mid, hi)

            i, j, k = lo, mid, lo
            
            while i < mid and j < hi:
                if nums[i] < nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1

            while i < mid:
                temp[k] = nums[i]
                i += 1
                k += 1

            while j < hi:
                temp[k] = nums[j]
                j += 1
                k += 1

            for idx in range(lo, hi):
                nums[idx] = temp[idx]

        sort(0, n)

        return nums
            