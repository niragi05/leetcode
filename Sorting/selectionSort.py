class Solution:
    def selectionSort(self, nums):
        n = len(nums)

        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                if nums[min_index] > nums[j]:
                    min_index = j
            
            nums[min_index], nums[i] = nums[i], nums[min_index]
        return nums