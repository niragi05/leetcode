class Solution:
    def reverseArray(self, arr, n):
        # Solution 1:
        l, r = 0, n - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
