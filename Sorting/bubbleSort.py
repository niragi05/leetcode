class Solution:
    def bubbleSort(self, nums):
        n = len(nums)

        for i in range(n - 1, -1, -1):
            did_swap = False
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    did_swap = True
            if did_swap is False:
                break
        return nums
    