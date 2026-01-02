class Solution:
    def quickSort(self, nums):
        n = len(nums)
        if n <= 1:
            return nums

        def partition(lo, hi):
            pivot = nums[hi]
            i = lo

            for j in range(lo, hi):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[hi] = nums[hi], nums[i]
            return i

        def sort(lo, hi):
            while lo < hi:
                p = partition(lo, hi)

                left = p - lo
                right = hi - p

                if left < right:
                    sort(lo, p - 1)
                    lo = p + 1
                else:
                    sort(p + 1, hi)
                    hi = p - 1

        sort(0, n - 1)
        return nums
